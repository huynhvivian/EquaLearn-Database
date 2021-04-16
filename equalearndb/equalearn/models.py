from django.db import models
#from django.db import User
import datetime

# Create your models here.

class User(models.Model):
    User_ID = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length = 12)
    email = models.CharField(max_length = 60)
    #Contract??

class Executive(User):
    position = models.CharField(max_length = 50)

class Tutor(User):
    # grade = models.CharField(max_length=50)
    # club = models.CharField(max_length=50)
    preference_online = models.CharField(max_length=50)
    date_started = models.DateField(auto_now_add = True)
    accepted = models.BooleanField(default = False)

class Client(User):
    referred_organization = models.CharField(max_length = 60)
    proof_of_low_income = models.BooleanField()
    accepted = models.BooleanField(default = False)

class Student(models.Model):
    student_id = models.AutoField(primary_key = True)
    user_id_client = models.ForeignKey(Client, related_name = 'students', on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    school = models.CharField(max_length = 50)
    class Meta:
        unique_together = (("name", "user_id_client"),)

    def getstudentname(self):
        return self.name

    def getschool(self):
        return self.school

class Subject(models.Model):
    subject_id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length = 20)
    grade_level = models.CharField(max_length = 5)
    class Meta:
        unique_together = (("course_name", "grade_level"),)

class Location(models.Model):
    library_name = models.CharField(primary_key = True, max_length = 100)
    def __str__(self):
        return self.library_name


class Session(models.Model):
    #Session ID, Tutor, Client, Student name, Date, start time, end time
    session_id = models.AutoField(primary_key = True)
    user_id_tutor = models.ForeignKey(Tutor, related_name = 'sessions', on_delete = models.CASCADE)
    user_id_client = models.ForeignKey(Client, related_name = 'sessions', on_delete = models.CASCADE)
    student_name = models.ForeignKey(Student, related_name = 'sessions', on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, related_name = 'sessions', on_delete = models.CASCADE)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50)

    def getstudent(self):
        return self.student_name.name

    def getclient(self):
        return self.student_name.user_id_client.name

    def getvolunteer(self):
        return self.user_id_tutor.name

    def getcoursename(self):
        return self.subject_id.course_name

    def getcourselevel(self):
        return self.subject_id.grade_level

    def totalhours(self):
        return (self.end_time - self.start_time).seconds // 3600

    def getstart(self):
        return (datetime.datetime.strftime(self.start_time, "%I:%M"))

    def getend(self):
        return (datetime.datetime.strftime(self.end_time, "%I:%M"))


class Takes(models.Model):
    takes_id = models.AutoField(primary_key = True)
    student_name = models.ForeignKey(Student, related_name = "takes", on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = "takes", on_delete = models.CASCADE)
    end_date = models.DateField(default = datetime.date(2021, 12, 31))
    current_tutor = models.ForeignKey(Tutor, related_name = "student_subject", on_delete = models.CASCADE, blank= True, null = True)
    class Meta:
        unique_together = (("student_name", "subject"),)

    def getclientemail(self):
        return self.student_name.user_id_client.email

    def getcoursename(self):
        return self.subject.course_name

    def getcourselevel(self):
        return self.subject.grade_level

    def getenddate(self):
        return self.end_date

    def getlocations(self):
        locationstr = ""
        for preflocation in preferred_student.objects.all():
            if (preflocation.student_name == self.student_name):
                locationstr = locationstr + preflocation.loc.__str__() + ", "

        return locationstr[:-2]

class Teaches(models.Model):
    teach_id = models.AutoField(primary_key = True)
    tutor_name = models.ForeignKey(Tutor, related_name = "teaches", on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, related_name = "teaches", on_delete = models.CASCADE)
    class Meta:
        unique_together = (("tutor_name", "subject"),)

class PendingSession(models.Model):
    sessions_id = models.AutoField(primary_key = True)
    user_id_tutor = models.ForeignKey(Tutor, related_name = 'pendingsessions', on_delete = models.CASCADE)
    user_id_client = models.ForeignKey(Client, related_name = 'pendingsessions', on_delete = models.CASCADE)
    takes_object = models.ForeignKey(Takes, related_name = 'pendingsessions', on_delete = models.CASCADE)
    location = models.CharField(max_length = 50)
    weekday = models.CharField(max_length = 15)
    start_time = models.TimeField()
    end_time = models.TimeField()

class preferred_student(models.Model):
    student_loc_id = models.AutoField(primary_key = True)
    student_name = models.ForeignKey(Student, related_name = "preferred_location", on_delete = models.CASCADE)
    loc = models.ForeignKey(Location, related_name = "preferred_student", on_delete = models.CASCADE)
    class Meta:
        unique_together = (("student_name", "loc"),)

class schedule_student(models.Model):
    student_schedule_id = models.AutoField(primary_key = True)
    student = models.ForeignKey(Student, related_name = "schedule", on_delete = models.CASCADE)
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    WEEKDAY_CHOICES = [
        (MONDAY, 0),
        (TUESDAY, 1),
        (WEDNESDAY, 2),
        (THURSDAY, 3),
        (FRIDAY, 4),
        (SATURDAY, 5),
        (SUNDAY, 6)
    ]
    weekday = models.CharField(max_length = 15, choices = WEEKDAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def gettimeslot(self):
        timestr = self.weekday + ": " + datetime.time.strftime(self.start_time, "%I:%m%p") + " - " + datetime.time.strftime(self.end_time, "%I:%m%p")
        return timestr
#class About(models.Model):
#    session_id = models.ForeignKey(Session, related_name = 'about', on_delete = models.CASCADE)
#    Subject.subject_name = models.ForeignKey(Subject, related_name = 'about_subjects', on_delete = models.CASCADE)
#    Subject.subject_grade = models.ForeignKey(Subject, related_name = 'about_grades', on_delete = models.CASCADE)
