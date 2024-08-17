from django.shortcuts import render


def assembly_pc(request):
    return render(request, 'users/assembly_pc.html')


def users(request):
    return render(request, 'users/users.html')