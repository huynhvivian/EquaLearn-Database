from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework import viewsets
import django.contrib.staticfiles
import random
import calendar
from datetime import date
from datetime import datetime
from datetime import timedelta
from .models import User
from .serializers import UserSerializer
from .models import Executive
from .serializers import ExecutiveSerializer
from .models import Tutor
from .serializers import TutorSerializer
from .models import Client
from .serializers import ClientSerializer
from .models import Student
from .serializers import StudentSerializer
from .models import Session
from .serializers import SessionSerializer
from .models import Subject
from .serializers import SubjectSerializer
from .models import Takes
from .serializers import TakesSerializer
from .models import Teaches
from .serializers import TeachesSerializer
from .models import Location
from .serializers import LocationSerializer
from.models import schedule_student
from .serializers import ScheduleStudentSerializer
from .models import preferred_student
from .serializers import PreferredStudentSerializer
from .models import PendingSession
from .serializers import PendingSessionSerializer



# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class ExecutiveViewSet(viewsets.ModelViewSet):
    queryset = Executive.objects.all().order_by('name')
    serializer_class = ExecutiveSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all().order_by('name')
    serializer_class = TutorSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('course_name')
    serializer_class = SubjectSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('library_name')
    serializer_class = LocationSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('session_id')
    serializer_class = SessionSerializer

class PendingSessionViewSet(viewsets.ModelViewSet):
    queryset = PendingSession.objects.all().order_by('sessions_id')
    serializer_class = PendingSessionSerializer

class TakesViewSet(viewsets.ModelViewSet):
    queryset = Takes.objects.all()
    serializer_class = TakesSerializer

class TeachesViewSet(viewsets.ModelViewSet):
    queryset = Takes.objects.all()
    serializer_class = TeachesSerializer

class PreferredStudentViewSet(viewsets.ModelViewSet):
    queryset = preferred_student.objects.all()
    serializer_class = PreferredStudentSerializer

class ScheduleStudentViewSet(viewsets.ModelViewSet):
    queryset = schedule_student.objects.all()
    serializer_class = ScheduleStudentSerializer

def executive_dashboard(request, id):
    #id = exec's user ID
    exec = Executive.objects.get(User_ID = id)
    return render(request, 'execdashboard.html', {'executive': exec})

def approve_volunteers(request, id):
    exec = Executive.objects.get(User_ID = id)
    unapprovedtutors = Tutor.objects.filter(accepted = False)
    return render(request, 'approvevolunteers.html', {'executive': exec, 'tutors': unapprovedtutors})

def approve_tutor(request, eid, tid):
    exec = Executive.objects.get(User_ID = eid)
    tutor = Tutor.objects.get(User_ID = tid)
    tutor.accepted = True
    tutor.save()
    return redirect('approve_volunteers', id=eid)

def view_pending_clients(request, id):
    exec = Executive.objects.get(User_ID = id)
    unapprovedclients = Client.objects.filter(accepted = False)
    return render(request, 'approveclients.html', {'executive': exec, 'clients': unapprovedclients})

def approve_client(request, eid, cid):
    client = Client.objects.get(User_ID = cid)
    client.accepted = True
    client.save()
    return redirect('view_pending_clients', id=eid)

def volunteer_dashboard(request, id):
    #id = volunteer's user ID
    tutor = Tutor.objects.get(User_ID = id)
    sessions = Session.objects.filter(user_id_tutor = id)
    return render(request, 'volunteerdashboard.html', {'sessions': sessions, 'tutor': tutor})

def volunteer_hours(request, id):
    tutor = Tutor.objects.get(User_ID = id)
    sessions = Session.objects.filter(status ='Verified', user_id_tutor = id)
    total = 0
    for session in sessions:
        total = total + session.totalhours()

    return render(request, 'viewhours.html', {'sessions': sessions, 'hours': total, 'tutor': tutor})

def session_signups(request, id):
    tutor = Tutor.objects.get(User_ID = id)
    takes = Takes.objects.filter(current_tutor = None)
    student_schedules = schedule_student.objects.all()
    student_locations = preferred_student.objects.all()
    return render(request, 'sessionsignups.html', {'takes': takes, 'tutor': tutor, 'schedules':student_schedules, 'student_locations': student_locations})

def view_pending_sessions(request, eid):
    exec = Executive.objects.get(User_ID = eid)
    pendingsessions = PendingSession.objects.all()
    return render(request, 'approvesessions.html', {'executive': exec, 'sessions': pendingsessions})

def approve_sessions(request, eid, psessionid):
    #We need: Client ID, location, timeslot, volunteer, and approve button. We get that information from takes and the volunteer...?
    pendingsession = PendingSession.objects.get(sessions_id = psessionid)

    takes = pendingsession.takes_object
    tutor = pendingsession.user_id_tutor

    endday = takes.end_date
    weekday = pendingsession.weekday
    start = pendingsession.start_time
    end = pendingsession.end_time
    loc = pendingsession.location

    currentday = datetime.date(datetime.now())

    #creating sessions
    while (calendar.day_name[currentday.weekday()] != weekday):
        currentday += timedelta(days = 1)

    currentday += timedelta(days = 7)
    #Then create a new session every week until the end day
    while (currentday < endday):
        Session.objects.create(
            user_id_tutor = tutor,
            user_id_client = takes.student_name.user_id_client,
            student_name = takes.student_name,
            subject_id = takes.subject,
            date = currentday,
            start_time = datetime.combine(currentday, start),
            end_time = datetime.combine(currentday, end),
            location = loc,
            status = "In Future"
            )
        currentday += timedelta(days = 7)

    #Delete pendingsessions object
    pendingsession.delete()
    return redirect('executive_dashboard', id=eid)

def sessions_signed_up(request, tid, takeid):
    #Make sessions from next-next session to the end... so we'd need current date, and the weekday
    currentday = datetime.date(datetime.now())
    thistake = Takes.objects.get(takes_id = takeid)
    thistake.current_tutor = Tutor.objects.get(User_ID = tid)
    thistake.save()
    endday = thistake.end_date


    loc = request.POST.get('chooseloc')
    time = request.POST.get('choosetime')
    if (loc == '' or time == ''):
        #no time or location filled out
        return redirect('volunteer_dashboard', id=tid)

    #parse time into a datetime object
    #Format of string: Weekday: HH:MMam - HH:MMpm
    #Splitting by whitespace gives "Weekday:", "HH:MM:am", "-", "HH:MMpm"
    weekday = (time.split()[0])[:-1]
    startstr = time.split()[1]
    endstr = time.split()[3]

    start = datetime.strptime(startstr, "%I:%m%p").time()
    end = datetime.strptime(endstr, "%I:%m%p").time()

    #create pendingsession object
    PendingSession.objects.create(
        user_id_tutor = thistake.current_tutor,
        user_id_client = thistake.student_name.user_id_client,
        takes_object = thistake,
        weekday = weekday,
        start_time = start,
        end_time = end,
        location = loc
    )

    return redirect('volunteer_dashboard', id=tid)

def approve_hours(request, eid):
    tutors = Tutor.objects.all()
    exec = Executive.objects.get(User_ID = eid)
    return render(request, 'approvehours.html', {'tutors': tutors, 'executive': exec})

def view_volunteer_hours(request, eid, tid):
    tutor = Tutor.objects.get(User_ID = tid)
    exec = Executive.objects.get(User_ID = eid)
    sessions = Session.objects.filter(status ='Verified', user_id_tutor = tid)
    total = 0
    for session in sessions:
        total = total + session.totalhours()
    return render(request, 'viewvolunteerhours.html', {'tutor': tutor, 'executive': exec, 'hours': total, 'sessions': sessions})

def client_dashboard(request, id):
    client = Client.objects.get(User_ID = id)
    sessions = Session.objects.all()
    return render(request, 'clientdashboard.html', {'sessions': sessions, 'client':client})

def editstudents(request, id):
    client = Client.objects.get(User_ID = id)
    students = Student.objects.filter(user_id_client=id)
    return render(request, 'editstudents.html', {'students': students, 'client': client})

def choosesubject(request, id):
    client = Client.objects.get(User_ID = id)
    subjects = Subject.objects.all()
    return(request, 'choosesubject.html', {'subjects': subjects, 'client': client})

def editsubject(request, id, name):
    student = Student.objects.filter(user_id_client=id, name = name)
    takes = Takes.objects.filter(student_name__in=student)
    client = Client.objects.get(User_ID = id)
#    for take in takes:
#        client = take.student_name.user_id_client
    return render(request, 'editsubject.html', {'takes': takes, 'client': client})

def client_edit_session(request, uid, sid):
    client = Client.objects.get(User_ID = uid)
    session = Session.objects.get(session_id = sid)
    locations = Location.objects.all()
    return render(request, 'clientchangesession.html', {'session': session, 'locations': locations, 'client': client})

def edit_sessions(request, uid, sid):
    tutor = Tutor.objects.get(User_ID = uid)
    session = Session.objects.get(session_id = sid)
    locations = Location.objects.all()
    return render(request, 'changesession.html', {'session': session, 'locations': locations, 'tutor': tutor})

def submit_edited_sessions(request, tid, sid):
    session = Session.objects.get(session_id = sid)
    if request.method == 'POST':
        newdate = request.POST.get('newdate', session.date)
        starttime = request.POST.get('newstart', session.start_time)
        endtime = request.POST.get('newend', session.end_time)
        loc = request.POST.get('changedloc', session.location)

        if (newdate != ''):
            session.date = newdate
        else:
            newdate = session.date

        if (starttime != ''):
            session.start_time = datetime.combine(datetime.strptime(newdate, '%Y-%m-%d'), datetime.strptime(starttime, '%H:%M').time())

        if (endtime != ''):
            session.end_time = datetime.combine(datetime.strptime(newdate, '%Y-%m-%d'), datetime.strptime(endtime, '%H:%M').time())

        if (session.location != loc):
            session.location = loc

        if (newdate == '' and starttime == '' and endtime == '' and session.location == loc):
            session.status = session.status
        else:
            session.status = "Pending Client Approval"

        session.save()

    return redirect('volunteer_dashboard', id=tid)

def client_submit_edited_sessions(request, tid, sid):
    session = Session.objects.get(session_id = sid)
    if request.method == 'POST':
        newdate = request.POST.get('newdate', session.date)
        starttime = request.POST.get('newstart', session.start_time)
        endtime = request.POST.get('newend', session.end_time)
        loc = request.POST.get('changedloc', session.location)

        if (newdate != ''):
            session.date = newdate
        else:
            newdate = session.date

        if (starttime != ''):
            session.start_time = datetime.combine(datetime.strptime(newdate, '%Y-%m-%d'), datetime.strptime(starttime, '%H:%M').time())

        if (endtime != ''):
            session.end_time = datetime.combine(datetime.strptime(newdate, '%Y-%m-%d'), datetime.strptime(endtime, '%H:%M').time())

        if (session.location != loc):
            session.location = loc

        if (newdate == '' and starttime == '' and endtime == '' and session.location == loc):
            session.status = session.status
        else:
            session.status = "Pending Tutor Approval"

        session.save()

    return redirect('client_dashboard', id=tid)

def cancel_session(request, tid, sid):
    session = Session.objects.get(session_id = sid)
    if request.method == 'POST':
        session.status = "Cancelled"
        session.save()
    return redirect('volunteer_dashboard', id=tid)


def client_cancel_session(request, tid, sid):
    session = Session.objects.get(session_id = sid)
    if request.method == 'POST':
        session.status = "Cancelled"
        session.save()
    return redirect('client_dashboard', id=tid)

def addstudent(request, id):
    client = Client.objects.get(User_ID = id)
    return render(request, 'addstudent.html', {'client': client})

def studentadded(request, id):
    client = Client.objects.get(User_ID = id)
    if request.method == 'POST':
        #if request.POST.get('fullname') and request.POST.get('school'):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        fullname = fname + " " + lname
        Student.objects.create(
            name = fullname,
            school = request.POST.get('school'),
            user_id_client = client
        )
            #student = Student()
            #student.name = request.POST.get('fullname')
            #student.school = request.POST.get('school')
            #student.user_id_client = client
            #student.save()

    return redirect('editstudents', id=id)

def changeschedule(request, cid, sname):
    client = Client.objects.get(User_ID = cid)
    student = Student.objects.get(name = sname, user_id_client = client)
    studentschedules = schedule_student.objects.filter(student = student)
    return render(request, 'changestudentschedule.html', {'client': client, 'student': student, 'schedules': studentschedules})

def schedulechanges(request, cid, sname):
    client = Client.objects.get(User_ID = cid)
    student = Student.objects.get(name = sname, user_id_client = client)
    newschedule = request.POST.getlist("schedule")
    oldschedule = schedule_student.objects.filter(student = student)
    for schedule in oldschedule:
        if schedule.getbasictimeslot() not in newschedule:
            #delete that one
            schedule.delete()
    for schedule in newschedule:
        notnew = True
        for oschedule in oldschedule:
            if oschedule.getbasictimeslot() == schedule:
                notnew = False
        if notnew:
            schedule_student.objects.create(
                student = student,
                weekday = schedule.split()[0],
                start_time = datetime.strptime(schedule.split()[1], "%I:%M%p").time(),
                end_time = datetime.strptime(schedule.split()[2], "%I:%M%p").time()
            )
    return redirect('editstudents', id=cid)
