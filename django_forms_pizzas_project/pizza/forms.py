from django import forms

class OrderForm(forms.Form):
    item1 = forms.CharField(label='Item 1', max_length=100)
    item2 = forms.CharField(label='Item 2', max_length=100)
    size = forms.ChoiceField(label='Size', choices=[('Small Size', 'Small'), ('Medium Size', 'Medium'), ('Large Size', 'Large')])