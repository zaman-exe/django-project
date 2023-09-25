from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from lemonapp.models import Menu

# Create your views here.
from .forms import ApplicationForm, PersonForm, BookingForm

def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)

def home(request):
    return render(request, "home.html", {})

def login(request):
    return render(request, "login.html", {}) 


def book(request):
    return HttpResponse('Make a booking')


def form(request): 
    form = ApplicationForm() 
    context = {'form': form}
    return render(request, 'forms.html', context) 

def person_form(request): 
    form = PersonForm() 
    if request.method == 'POST':
        form= PersonForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'person_form': form}
    return render(request, 'forms.html', context) 

def booking_form(request): 
    form = BookingForm() 
    if request.method == 'POST':
        form= BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'booking_form': form}
    return render(request, 'forms.html', context) 

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def about(request): 
    return render(request, 'about.html')

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 
     