from django.shortcuts import render
from django.http import HttpResponse
import django.contrib.staticfiles
from .models import User
from .models import Tutor
from .models import Client
from .models import Student
from .models import Session
from .models import Subject



# Create your views here.
def volunteer_dashboard(request):
    sessions = Session.objects.all()
    return render(request, 'volunteerdashboard.html', {'sessions': sessions})
