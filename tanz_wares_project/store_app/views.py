from django.forms import forms
from django.shortcuts import render, redirect
from django import forms
from .forms import RegistrationForm, LoginForm
from .models import User, Item
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'login_form':LoginForm()
    }
    return render(request, 'index.html', context)

def registration(request):
    context={
        'registration_form':RegistrationForm()
    }
    return render(request, 'registration.html', context)

def register(request):
    registration_form=RegistrationForm(request.POST)
    errors= User.objects.register(registration_form.data)
    if request.method!= 'POST':
        return redirect('/registration')
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')
    if registration_form.is_valid():
        new_user= User.objects.create(
            first_name= registration_form.data['first_name'],
            last_name=registration_form.data['last_name'],
            email=registration_form.data['email'],
            pw= bcrypt.hashpw(registration_form.data['pw'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['id']= new_user.id
        return redirect('/home')

def verify(request):
    login_form=LoginForm(request.POST)
    errors= User.objects.verify_login(login_form.data)
    if request.method!= 'POST':
        return redirect('/')
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if login_form.is_valid():
        logged_user=User.objects.filter(email=login_form.data['email'])[0]
        request.session['id']=logged_user.id
        return redirect('/home')
        
def home(request):
    context={
        'user': User.objects.get(id=request.session['id']),
        'items':Item.objects.all()
    }
    return render(request, 'home.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')