from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .forms import MyUserCreationForm, MyUserCreationForm1
from django.template.loader import render_to_string
from django.contrib.auth.models import auth, User
from django.core.mail import EmailMessage
from django.conf import settings



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

def registration1(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Huff ,Username already exist')
            return redirect("register1")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Come On, Email was already Taken !')
            return redirect("register1")
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            mydict = {'username': username, 'email': email, 'password': password}
            html_template = 'accounts/register_email.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Welcome to OLMS'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()

            messages.success(request,'You have successfully registered')
            return redirect("Home")
    else:
        return render(request, 'accounts/registration1.html')


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