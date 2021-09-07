from django.db import models
import bcrypt, re

# Create your models here.
class UserValidation(models.Manager):
    def verify_login(self, post):
        errors={}
        user_logged= User.objects.filter(email=post['email'])
        if len(post['email'])== 0:
            errors['email']='Enter an email please!'
        elif len(user_logged)==0:
            errors['dne']='No user with that email'
        if len(post['password']) == 0:
            errors['password']='Password needed to continue!'
        elif not bcrypt.checkpw(post['password'].encode(), user_logged[0].password.encode()):
            errors['incorrect']='Password/Email combination incorrect'
        return errors
        
    def register(self, post):
        email_ver= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(post['first_name']) <2 or len(post['last_name']) <2:
            errors['name']='Name length too short!'
        if len(post['password'])==0:
            errors['nan']='Password needed to continue!'
        elif post['password'] != post['password_confirm']:
            errors['password']='Passwords do not match!'
        if not email_ver.match(post['email']):
            errors['email']= 'Email format incorrect!'


class User(models.Model):
    first_name= models.CharField(max_length=60)
    last_name= models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    password= models.CharField(max_length=20)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= UserValidation()