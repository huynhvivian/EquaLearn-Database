from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from equalearn.models import User as EqualearnUser
from equalearn.models import Tutor
from equalearn.models import Client
from equalearn.models import Executive

def login_page(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # the code below doesn't work :(
        if user.__class__.__name__ == 'Executive':
            return redirect('execdashboard.html', id=user.User_ID)
        if user.__class__.__name__ == 'Tutor':
            return redirect('tutordashboard.html', id=user.User_ID)
        if user.__class__.__name__ == 'Client':
            return redirect('clientdashboard.html', id=user.User_ID)
    else:
        # Return an 'invalid login' error message.
        ...

def pagelogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        newuser = EqualearnUser.objects.create()
        return redirect('choose_account', id=newuser.User_ID)
    return render(request, 'signup.html')

def choose_account(request, id):
    user = EqualearnUser.objects.get(User_ID = id)
    return render(request, 'chooseaccount.html', {'user': user})

def client_app(request, id):
    client = EqualearnUser.objects.get(User_ID = id)
    return render(request, 'clientapplication.html', {'client': client})

def tutor_app(request, id):
    tutor = EqualearnUser.objects.get(User_ID = id)
    return render(request, 'tutorapplication.html', {'tutor': tutor})

def choose_tutor(request, id):
    if request.method == 'POST':
        user = EqualearnUser.objects.get(User_ID = id)
        tutor = Tutor()
        tutor.User_ID = user.User_ID
        tutor.name = request.POST.get('fullname')
        tutor.grade = request.POST.get('grade')
        tutor.club = request.POST.get('club')

        tutor.preference_online = request.POST.get("preference"),
        # tutor.email = user.email

        tutor.save()
        
        # if (p == "live"):
            # preference = False
        # else:
            # preference = True
        
        # tutor.preference_online = preference

        # tutor = Tutor.objects.create(
        #     User_ID = user.User_ID,
        #     name = user.name,
        #     email = user.email,
        #     phone_number = request.POST.get("number"),
        #     preference_online = preference
        # )
        
    return redirect('volunteer_dashboard', id=id)

def choose_exec(request, id):
    if request.method == 'POST':
        user = EqualearnUser.objects.get(User_ID = id)
        exec = Executive.objects.create(
            User_ID = user.User_ID,
            name = user.name,
            email = user.email,
            phone_number = user.phone_number,
            position = "placeholder"
        )
    return redirect('executive_dashboard', id=id)

def choose_client(request, id):
    if request.method == 'POST':
        user = EqualearnUser.objects.get(User_ID = id)
        exec = Client.objects.create(
            User_ID = user.User_ID,
            name = user.name,
            email = user.email,
            phone_number = request.POST.get("number"),
            referred_organization = request.POST.get("org"),
            proof_of_low_income = True
        )
    return redirect('client_dashboard', id=id)
