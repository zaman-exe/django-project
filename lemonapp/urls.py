from django.urls import path
from . import views

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
    path('', views.home, name="home"),
    path('login/', views.login, name="menu"),  
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"), 
    path('about/', views.about,name="about"), 
    path('person_form/', views.person_form), 
    path('booking_form/', views.booking_form)
]