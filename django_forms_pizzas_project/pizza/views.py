from django.shortcuts import render
from .forms import OrderForm

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    form = OrderForm()
    return render(request, 'pizza/order.html', {'orderform':form})