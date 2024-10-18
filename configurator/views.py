from django.views.generic import TemplateView, FormView, ListView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import ConfiguratorForm
from django.urls import reverse_lazy
from configurator.models import AssemblerPC, CPU, GPU, Motherboard, RAM, StorageDrive, PowerSupply, CoolingSystem, Case
from django.http import HttpResponse
from rest_framework import viewsets
from configurator.serializers import CpuSerializer


class HomePageView(TemplateView):
    template_name = 'configurator/home_page.html'


class AssemblerPCView(FormView):
    form_class = ConfiguratorForm
    template_name = 'configurator/assembler_pc.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        pass


def get_price(request):
    model = request.GET.get('model')
    id = request.GET.get('id')
    models_components = {
        'cpu': CPU,
        'gpu': GPU,
        'motherboard': Motherboard,
        'ram': RAM,
        'storage_drive': StorageDrive,
        'power_supply': PowerSupply,
        'cooling_system': CoolingSystem,
        'case': Case,
    }
    if model in models_components:
        price = models_components[model].objects.get(id=id).price
        return HttpResponse(price)
    return HttpResponse('Компонент не найден', status=400)


class ApiCpuViewSet(viewsets.ModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CpuSerializer


class PCList(ListView):
    model = AssemblerPC
    template_name = 'configurator/PCList.html'
    paginate_by = 9


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form
    })