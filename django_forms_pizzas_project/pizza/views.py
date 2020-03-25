from django.shortcuts import render
from .forms import OrderForm, MultipleItemsForm
from django.forms import formset_factory
from .models import Order

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultipleItemsForm()
    if request.method == 'POST':
        # filled_form = OrderForm(request.POST, request.FILES)
        filled_form = OrderForm(request.POST) # create a form object with request.POST data
        if filled_form.is_valid():
            created_order = filled_form.save() # to save the submitted data in DB, can be verified in admin
            created_order_pk = created_order.id
            note = 'Thanks for ordering! Your delivery for %s %s and %s is on its way' %(filled_form.cleaned_data['size'], 
                    filled_form.cleaned_data['item1'],
                    filled_form.cleaned_data['item2'])
            new_form = OrderForm()
            return render(request, 'pizza/order.html', {'created_order_pk': created_order_pk, 'orderform':new_form, 'note': note, 'multiple_form': multiple_form})
    else:
        form = OrderForm()
        return render(request, 'pizza/order.html', {'orderform':form, 'multiple_form': multiple_form})

def items(request):
    number_of_items = 2
    filled_multiple_items_form = MultipleItemsForm(request.GET)
    if filled_multiple_items_form.is_valid():
        number_of_items = filled_multiple_items_form.cleaned_data['number']
    ItemFormSet = formset_factory(OrderForm, extra=number_of_items)
    formset = ItemFormSet() # initially should be empty
    if request.method == 'POST':
        filled_formset = ItemFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['item1']) # logging output on terminal for testing
            note = 'Items have been ordered'
        else:
            note = 'Order was not created, please try again'
        return render(request, 'pizza/pizzas.html', {'note': note, 'formset': formset})
    else: # GET
        return render(request, 'pizza/pizzas.html', {'formset': formset})

def edit_order(request, pk):
    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        filled_form = OrderForm(request.POST, isinstance=order)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
    return render(request, 'pizza/edit_order.html', {'orderform': form, 'order': order})