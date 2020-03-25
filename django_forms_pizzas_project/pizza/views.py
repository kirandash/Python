from django.shortcuts import render
from .forms import OrderForm

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        # filled_form = OrderForm(request.POST, request.FILES)
        filled_form = OrderForm(request.POST) # create a form object with request.POST data
        if filled_form.is_valid():
            note = 'Thanks for ordering! Your delivery for %s %s and %s is on its way' %(filled_form.cleaned_data['size'], 
                    filled_form.cleaned_data['item1'],
                    filled_form.cleaned_data['item2'])
            new_form = OrderForm()
            return render(request, 'pizza/order.html', {'orderform':new_form, 'note': note})
    else:
        form = OrderForm()
        return render(request, 'pizza/order.html', {'orderform':form})