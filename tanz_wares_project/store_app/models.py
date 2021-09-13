from django.db import models
import bcrypt, re

from django.db.models.deletion import CASCADE
from .forms import *

# Create your models here.
class UserValidation(models.Manager):
    def verify_login(self, post):
        errors={}
        user_logged= User.objects.filter(email=post['email'])
        if len(post['email'])== 0:
            errors['email']='Enter an email please!'
        elif len(user_logged)==0:
            errors['dne']='No user with that email'
        if len(post['pw']) == 0:
            errors['pw']='Password needed to continue!'
        elif not bcrypt.checkpw(post['pw'].encode(), user_logged[0].pw.encode()):
            errors['incorrect']='Password/Email combination incorrect'
        return errors
        
    def register(self, post):
        registration_form=RegistrationForm(post)
        email_ver= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(registration_form.data['first_name']) <2 or len(registration_form.data['last_name']) <2:
            errors['name']='Name length too short!'
        if registration_form.data['pw'] != registration_form.data['pw_c']:
            errors['pw']='Passwords do not match!'
        if not email_ver.match(registration_form.data['email']):
            errors['email']= 'Email format incorrect!'
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=60)
    last_name= models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    pw= models.CharField(max_length=20)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= UserValidation()

    def __str__(self):
        return self.first_name

class Item(models.Model):
    name= models.CharField(max_length=25)
    price= models.FloatField()
    desc=models.TextField()
    image=models.ImageField(default='default.jpg', upload_to='item_images')
    fav_by=models.ManyToManyField(User, related_name='fav_item')

    def __str__(self):
        return self.name