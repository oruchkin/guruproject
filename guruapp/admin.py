from django.contrib import admin
from .models import (Shop, City, Street)


@admin.register(Shop)
class Shop_Admin(admin.ModelAdmin):
    list_display = ['title','city', 'street','house','time_open', 'time_closed']


@admin.register(City)
class Town_Admin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Street)
class Street_Admin(admin.ModelAdmin):
    list_display = ['title']