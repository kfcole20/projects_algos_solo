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

class CheckoutForm(forms.Form):
    name_on_card=forms.CharField(max_length=255, label='Name on Card:')
    card_num=forms.IntegerField(label='Card Number:', max_value=6999999999999999)
    zipcode=forms.IntegerField(label='Zipcode', max_value=99999)
