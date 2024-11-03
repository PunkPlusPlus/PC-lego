from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import logout



def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш аккаунт создан! Теперь вы можете войти.')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


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
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('home_page')


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
    return render(request, 'users/password_change.html', {
        'form': form
    })