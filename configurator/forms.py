from django import forms
from configurator.interfaces import ComponentTypes


class ComponentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=ComponentTypes.choices())
    brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
