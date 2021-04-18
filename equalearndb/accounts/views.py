from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from equalearn.models import User as EqualearnUser
from equalearn.models import Tutor
from equalearn.models import Client
from equalearn.models import Executive
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_page(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
 
def pagelogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # fname = form.cleaned_data.get('first_name')
            # lname = form.cleaned_data.get('last_name')
            # name = fname + " " + lname
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            newuser = EqualearnUser.objects.create(username = username, email = email, phone_number="x")
            return redirect('choose_account', id=newuser.User_ID)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         raw_password = request.POST.get('password')
#         user = authenticate(username=username, password=raw_password)
#         # login(request, user)
#         newuser = EqualearnUser.objects.create(username=username, email=email)
#         newuser.save()
#         return redirect('choose_account', id=newuser.User_ID)
#     return render(request, 'signup.html')

def choose_account(request, id):
    user = EqualearnUser.objects.get(User_ID = id)
    return render(request, 'chooseaccount.html', {'user': user})

def client_app(request, id):
    client = EqualearnUser.objects.get(User_ID = id)
    return render(request, 'clientapplication.html', {'client': client})

def tutor_app(request, id):
    tutor = EqualearnUser.objects.get(User_ID = id)
    return render(request, 'tutorapplication.html', {'tutor': tutor})

def exec_app(request, id):
    exec = EqualearnUser.objects.get(User_ID = id)
    return render(request, 'execapplication.html', {'exec': exec})

def choose_tutor(request, id):
    if request.method == 'POST':
        user = EqualearnUser.objects.get(User_ID = id)
        user.usertype = "tutor"
        user.save()

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone = request.POST.get("number")

        tutor = Tutor.objects.create(
         User_ID = user.User_ID,
         username = user.username,
         usertype = "tutor",
        #  name = user.name,
         name = fname + " " + lname,
         email = user.email,
         phone_number = phone, 
         preference_online = request.POST.get("preference")
        )

    return redirect('login')

def choose_exec(request, id):
    if request.method == 'POST':
        user = EqualearnUser.objects.get(User_ID = id)
        user.usertype = "executive"
        user.save()

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone = request.POST.get("number")

        exec = Executive.objects.create(
            User_ID = user.User_ID,
            username = user.username,
            usertype = "executive",
            # name = user.name,
            name = fname + " " + lname,
            email = user.email,
            phone_number = phone,
            position = request.POST.get("position")
        )
    return redirect('login')

def choose_client(request, id):
    if request.method == 'POST':
        user = EqualearnUser.objects.get(User_ID = id)
        user.usertype = "client"
        user.save()

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone = request.POST.get("number")

        exec = Client.objects.create(
            User_ID = user.User_ID,
            username = user.username,
            usertype = "client",
            # name = user.name,
            name = fname + " " + lname,
            email = user.email,
            phone_number = phone,
            referred_organization = request.POST.get("org"),
            proof_of_low_income = True
        )
    return redirect('login')

def getusername(request):
    return HttpResponseRedirect(reverse('home', args=[request.user.username]))

def home(request, username):
    #username = HttpResponseRedirect(reverse())
    user = EqualearnUser.objects.get(username = username)
    type = user.usertype
    if (type == "executive"):
        return redirect('executive_dashboard', id=user.User_ID)
    elif (type == "tutor"):
        return redirect('volunteer_dashboard', id = user.User_ID)
    elif (type == "client"):
        return redirect('client_dashboard', id = user.User_ID)
    else:
        return redirect('login')
