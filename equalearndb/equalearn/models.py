from django.db import models
#from django.db import User

# Create your models here.

class User(models.Model):
    User_ID = models.IntegerField(unique = True)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length = 12)
    email = models.CharField(max_length = 60)
    #Contract??

class Tutor(User):
    preference_online = models.BooleanField()
    date_started = models.DateField(auto_now_add = True)

class Client(User):
    referred_organization = models.CharField(max_length = 60)
    proof_of_low_income = models.BooleanField()

class Student(models.Model):
    user_id_client = models.ForeignKey(Client, related_name = 'students', on_delete = models.CASCADE)
    name = models.CharField(max_length = 50, unique = True)
    school = models.CharField(max_length = 50)

class Subject(models.Model):
    subject_id = models.IntegerField(unique = True)
    course_name = models.CharField(max_length = 20)
    grade_level = models.CharField(max_length = 5)

class Session(models.Model):
    #Session ID, Tutor, Client, Student name, Date, start time, end time
    session_id = models.IntegerField(unique = True)
    user_id_tutor = models.ForeignKey(Tutor, related_name = 'sessions', on_delete = models.CASCADE)
    user_id_client = models.ForeignKey(Client, related_name = 'sessions', on_delete = models.CASCADE)
    student_name = models.ForeignKey(Student, related_name = 'sessions', on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, related_name = 'sessions', on_delete = models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50)

    def getstudent(self):
        return self.student_name.name

    def getcoursename(self):
        return self.subject_id.course_name

    def getcourselevel(self):
        return self.subject_id.grade_level

#class About(models.Model):
#    session_id = models.ForeignKey(Session, related_name = 'about', on_delete = models.CASCADE)
#    Subject.subject_name = models.ForeignKey(Subject, related_name = 'about_subjects', on_delete = models.CASCADE)
#    Subject.subject_grade = models.ForeignKey(Subject, related_name = 'about_grades', on_delete = models.CASCADE)
