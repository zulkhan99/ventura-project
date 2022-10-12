from django.shortcuts import render
from django.http import HttpResponse, request
from django.template import loader
from django.shortcuts import render
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'home.html', {'date_placeholder': date_placeholder()})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def date_placeholder():
    today = date.today()
    today = today.strftime("%m/%d/%Y")
    return today