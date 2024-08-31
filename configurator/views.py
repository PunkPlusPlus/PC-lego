from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ConfiguratorForm


class HomePageView(TemplateView):
    template_name = 'configurator/home_page.html'


class AssemblerPCView(FormView):
    form_class = ConfiguratorForm
    template_name = 'configurator/assembler_pc.html'
    success_url = 'home_page'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        pass



