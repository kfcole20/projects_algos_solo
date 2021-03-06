from typing import ContextManager
from django.forms import forms
from django.shortcuts import render, redirect
from django import forms
from .forms import CheckoutForm, RegistrationForm, LoginForm
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
        'items':Item.objects.all(),
        
    }
    return render(request, 'home.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def add_favorite(request, item_id):
    this_item=Item.objects.get(id=item_id)
    user=User.objects.get(id=request.session['id'])
    this_item.fav_by.add(user)
    return redirect('/home')

def remove_favorite(request, item_id):
    this_item=Item.objects.get(id=item_id)
    user=User.objects.get(id=request.session['id'])
    this_item.fav_by.remove(user)
    return redirect('/favorites_view')

def fav_view(request):
    user=User.objects.get(id=request.session['id'])
    context={
        'items':user.fav_item.all(),
        'user':user
    }
    return render(request, 'favorites.html', context)

def cart_view(request):
    user=User.objects.get(id=request.session['id'])
    items= user.cart_item.all()
    total=0
    for item in items:
        total+=item.price
    context={
        'items':items,
        'total':total
    }
    request.session['total']=total
    return render(request, 'cart.html', context)

def add_cart(request, item_id):
    this_item=Item.objects.get(id=item_id)
    user=User.objects.get(id=request.session['id'])
    this_item.added_item.add(user)
    return redirect('/home')

def remove_cart(request, item_id):
    this_item=Item.objects.get(id=item_id)
    user=User.objects.get(id=request.session['id'])
    this_item.added_item.remove(user)
    return redirect('/cart_view')

def checkout(request):
    checkoutForm=CheckoutForm()
    user=User.objects.get(id=request.session['id'])
    items= user.cart_item.all()
    context={
        'checkoutForm':checkoutForm,
        'total':request.session['total'],
        'items':items
    }
    return render(request, 'checkout.html', context)

def verify_card(request):
    user=User.objects.get(id=request.session['id'])
    user.cart_item.clear()
    return redirect('/success')

def success(request):
    return render(request, 'success.html')