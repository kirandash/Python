from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<p>home view</p>')

def pet_detail(request, id):
    return HttpResponse('<p>pet_detail view with the id {}</p>'.format(id)) # {} servers as placeholder for format(id)