from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm



# Create your views here.

def registration(req):
    if req.method=='POST':
        #userform = UserCreationForm(req.POST)
        userform = MyUserCreationForm(req.POST)
        if userform.is_valid():
            user = userform.save()  # here we save data of user model only
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.role=userform.cleaned_data.get('role')
            user.save()
            messages.success(req,'You have successfully registered')
            return redirect('Home')
    else:
        #userform = UserCreationForm()
        userform = MyUserCreationForm()
    data = {'userform':userform}
    return render(req,'accounts/registration.html',data)



def mylogin(req):
    if req.method=='POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(req,user)
            messages.success(req,'Login Successfully....')
            return redirect('Home')
        else:
            messages.error(req,'Invalid Username or password....')
            return redirect('login')
    elif req.method=='GET':
        loginform = AuthenticationForm()
        data ={'loginform':loginform}
        return render(req,'accounts/login.html',data)


def mylogout(req):
    req.user=None
    logout(req)
    messages.success(req,'Logout Successfully....')
    return redirect('Home')