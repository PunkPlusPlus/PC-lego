from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.urls import reverse_lazy


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        return super().form_valid(form)


def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            messages.success(request, 'Logged in!')
            return redirect('/')
        else:
            messages.error(request,'Failed(')
    return render(request, 'registration/login.html')