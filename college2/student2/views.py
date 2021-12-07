from django.db.models import Avg,Count,Max,Min,Sum
from django.conf import settings
from django.shortcuts import render,redirect
from.forms import studentForm, RegistrationForm
from.models import studentdata
from django.contrib.auth.models import User
from.forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail




def home(request):
    return render(request,'home.html')

def index(request):
    college2=studentdata.objects.all
    return render(request,'index.html',{'college2':college2})


def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email=request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                user = User.objects.create_user(username=name, email=email, password=password)

                stu = studentdata.objects.create(
                    mobile=request.POST.get('mobile'),
                    address=request.POST.get('address'),
                    gender=request.POST.get('gender'),
                    country = request.POST.get('country'),
                    User=user,
                    marks_percentage=0)
                send_mail(
                     'Registration successful',
                     'Registration Successfull login link:http://127.0.0.1:8000/students/login/',
                     'sivakumarvaddipalli@gmail.com',
                     [email],
                      )
                return redirect('/student2/index/')
            else:
                form = RegistrationForm()
                return render(request, 'register.html',{'Comment': 'Enter valid password','form':form})

    form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def delete(request, id):
    college2=studentdata.objects.get(id=id)
    college2.delete()
    return redirect('/student2/index/')

def edit(request, id):
    college2 = studentdata.objects.get(id = id)
    form = studentForm(instance=college2)
    return render(request, 'update.html',{'form':form, 'id':id})


def update(request, id):
    college2=studentdata.objects.get(id=id)
    form=studentForm(request.POST, instance=college2)
    if form.is_valid():
        form.save()
        return redirect('/student2/index/')
    return render(request, 'update.html',{'form':form})

def login(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(user)
        if user:

            return redirect('/student2/index/')
    return render(request,'login.html',{})

def logout(request):
    logout(request)
    return redirect('/student2/login/')

