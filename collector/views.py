from django.shortcuts import render


def components(request):
    return render(request, 'collector/components.html')


def matching_table(request):
    return render(request, 'collector/matching_table.html')


def assembly_pc(request):
    return render(request, 'collector/assembly_pc.html')