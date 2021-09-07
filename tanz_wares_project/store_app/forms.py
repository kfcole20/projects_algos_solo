from django import forms

class RegistrationForm(forms.Form):
    first_name= forms.CharField(max_length=60)
    last_name= forms.CharField(max_length=60)
    email=forms.CharField(max_length=60)
    password= forms.CharField(widget=forms.PasswordInput())
    password_confirm= forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    email=forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput())