from django.shortcuts import render
from django.http import HttpResponse


def assembly_pc(request):
    return render(request, 'users/assembly_pc.html')


def users(request):
    return render(request, 'users/users.html')


def reg_form(request):
    username = request.POST.get('name', 'undefined')
    email = request.POST.get('email', 'undefined')
    password = request.POST.get('password', 'undefined')
    return HttpResponse(f"<div>Name: {username}  Email: {email} Password: {password}<div>")