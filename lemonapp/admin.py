from django.contrib import admin
from .models import Person,Booking, Menu
# Register your models here.
admin.site.register(Person)
admin.site.register(Menu)
admin.site.register(Booking)