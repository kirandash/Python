from django import forms
from .models import Order, Size

# class OrderForm(forms.Form):
#     # item1 = forms.CharField(label='Item 1', max_length=100, widget = forms.Textarea)
#     # item1 = forms.CharField(label='Item 1', max_length=100, widget = forms.PasswordInput)
#     # items = forms.MultipleChoiceField(choices=[('i1', 'Item1'), ('i2', 'Item2'), ('i3', 'Items3')], widget=forms.CheckboxSelectMultiple)
#     item1 = forms.CharField(label='Item 1', max_length=100)
#     item2 = forms.CharField(label='Item 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small Size', 'Small'), ('Medium Size', 'Medium'), ('Large Size', 'Large')])

class OrderForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)
    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect) # Another way of adding widget

    # image = forms.ImageField()

    class Meta:
        model = Order
        fields = ['item1', 'item2', 'size'] # should match the field names defined for class Order in models.py file
        labels = {'item1': 'Item One', 'item2': 'Item Two' } # Adding custom labels to model fields
        # widgets = {'item1': forms.Textarea, 'size': forms.CheckboxSelectMultiple}

class MultipleItemsForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)