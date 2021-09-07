from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    form= LoginForm()
    context={
        'form':form
    }
    return render(request, 'index.html', context)

def verify(request):
    errors={}

def registration(request):
    form=RegistrationForm()
    context={
        'form':form
    }
    return render(request, 'registration.html', context)

def register(request):
    errors= User.objects.register(request.POST)
    if request.method!= 'POST':
        return redirect('/registration')
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')
    new_user= User.objects.create(
        first_name= request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    )
    request.session['id']= new_user.id
    return redirect('/')

