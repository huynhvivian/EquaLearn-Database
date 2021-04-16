from django.contrib import admin
from .models import User
from .models import Client
from .models import Tutor
from .models import Student
from .models import Subject
from .models import Session
from .models import Takes
from .models import Teaches
from .models import preferred_student
from .models import Location
from .models import schedule_student
from .models import PendingSession
from .models import Executive
# Register your models here.
admin.site.register(User)
admin.site.register(Executive)
admin.site.register(Client)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Session)
admin.site.register(Takes)
admin.site.register(Teaches)
admin.site.register(preferred_student)
admin.site.register(Location)
admin.site.register(schedule_student)
admin.site.register(PendingSession)
