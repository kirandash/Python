from django.contrib import admin

# Register your models here.
from .models import Pet # import Pet Model

@admin.register(Pet) # decorator to register model to be used for admin

class PetAdmin(admin.ModelAdmin):
    # overwrite ModelAdmin class
    # pass # pass is for making PetAdmin a valid Python class
    list_display = ['name', 'species', 'breed', 'age', 'sex'] # by default, the admin list view just shows pet object. We are controlling exactly what to show on that screen. with the list_display attr

