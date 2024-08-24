from django.shortcuts import render
from django.views.generic import TemplateView
from configurator.forms import ComponentForm
from configurator.models import Component, Brand


def create_component(request):
    if request.method == 'POST':
        data = ComponentForm(request.POST)
        if data.is_valid():
            component = Component()
            component.name = data.cleaned_data['name']
            component.brand, created = Brand.objects.get_or_create(name=data.cleaned_data['brand'])
            component.price = data.cleaned_data['price']
            component.type = data.cleaned_data['type']
            component.save()

    form = ComponentForm()
    return render(request, 'index.html', {'form': form})