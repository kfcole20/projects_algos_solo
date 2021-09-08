from django import forms

class RegistrationForm(forms.Form):
    first_name= forms.CharField(label="First Name", max_length=60, min_length=2)
    last_name= forms.CharField(label="Last Name", max_length=60, min_length=2)
    email=forms.CharField(max_length=60)
    pw= forms.CharField(label="Password", widget=forms.PasswordInput())
    pw_c= forms.CharField(label="Confirm Password",widget=forms.PasswordInput())

class LoginForm(forms.Form):
    email=forms.CharField(max_length=60)
    pw = forms.CharField(label="Password",widget=forms.PasswordInput())