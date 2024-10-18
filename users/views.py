from django.views.generic import CreateView
from .forms import RegisterUserForm
from django.urls import reverse_lazy


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    # success_url = reverse_lazy('login')


    def form_valid(self, form):
        return super().form_valid(form)