from django.contrib import admin
from .models import User
from .models import Client
from .models import Tutor
from .models import Student
from .models import Subject
from .models import Session
# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Session)
