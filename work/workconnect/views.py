from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, RegistrationModel
from .models import RegistrationData
from django.views.generic import ListView

# Create your views here.
def basehome(request):
    return render(request, 'home.html')

def contact(request):

    context = {
        'form': RegistrationForm,

    }
    return render(request, 'contact.html', context)

def adduser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        register = RegistrationData(name=form.cleaned_data['name'],
                                    email=form.cleaned_data['email'],
                                    subject=form.cleaned_data['subject'],
                                    message=form.cleaned_data['message']
                                    )

        register.save()
        messages.add_message(request, messages.SUCCESS,  "Your message has been sent successfully")

    return redirect('contact')

def aanmelden(request):
    return render(request, 'aanmelden.html')
def overons(request):
    return render(request, 'overons.html')
def login(request):
    return render(request, 'login.html')
