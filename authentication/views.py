from telnetlib import STATUS
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken')
        else:
            myuser = User.objects.create_user(username=username,password=pass1,email=email)
            
            
            # myuser.is_active = False
            
            myuser.save()
            messages.success(request, "Your Account has been created")
            return HttpResponseRedirect('signin')

    return render(request,"authentication/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']

        user=auth.authenticate(username=username,password=pass1)

        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('app1')

        else:
            messages.info(request,"Incorrect credentials")
            return redirect('signin')
    return render(request,"authentication/signin.html")

def signout(request):
    auth.logout(request)
    return redirect(home)