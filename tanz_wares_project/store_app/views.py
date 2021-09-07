from django.shortcuts import render
from .forms import RegistrationForm, LoginForm
from .models import User

# Create your views here.
def index(request):
    form= LoginForm()
    context={
        'form':form
    }
    return render(request, 'index.html', context)

def verify(request):
    errors={}