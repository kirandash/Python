from django.contrib import admin

# Register your models here.
from .models import Country

@admin.register(Country) # decorator to register model to be used for admin

class CountryAdmin(admin.ModelAdmin):
    # overwrite ModelAdmin class
    # pass # pass is for making CountryAdmin a valid Python class, if there is no other code.
    list_display = ['code', 'pinned'] # by default, the admin list view just shows countries object. We are controlling exactly what to show on that screen. with the list_display attr
    