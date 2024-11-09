from django.views.generic import TemplateView, FormView, ListView
from .forms import ConfiguratorForm
from django.urls import reverse_lazy
from configurator.models import AssemblerPC, CPU, GPU, Motherboard, RAM, StorageDrive, PowerSupply, CoolingSystem, Case, \
    TypePC
from django.http import HttpResponse
from rest_framework import viewsets
from configurator.serializers import CpuSerializer


class HomePageView(TemplateView):
    model = TypePC
    template_name = 'configurator/home_page.html'


class AssemblerPCView(FormView):
    form_class = ConfiguratorForm
    template_name = 'configurator/assembler_pc.html'
    success_url = reverse_lazy('home_page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        type_id = self.request.GET.get('type')
        form.fields['cpu'].queryset = CPU.objects.filter(type_pc_id=type_id)
        form.fields['gpu'].queryset = GPU.objects.filter(type_pc_id=type_id)
        form.fields['motherboard'].queryset = Motherboard.objects.filter(type_pc_id=type_id)
        form.fields['ram'].queryset = RAM.objects.filter(type_pc_id=type_id)
        form.fields['storage_drive'].queryset = StorageDrive.objects.filter(type_pc_id=type_id)
        form.fields['power_supply'].queryset = PowerSupply.objects.filter(type_pc_id=type_id)
        form.fields['cooling_system'].queryset = CoolingSystem.objects.filter(type_pc_id=type_id)
        form.fields['case'].queryset = Case.objects.filter(type_pc_id=type_id)
        return form

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(show_modal=True))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_modal'] = kwargs.get('show_modal', False)
        return context


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
    paginate_by = 1

    def get_ordering(self):
        ordering = self.request.GET.get('sort-by')
        return ordering

