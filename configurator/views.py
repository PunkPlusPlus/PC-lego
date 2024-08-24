from django.shortcuts import render


def components(request):
    return render(request, 'configurator/components.html')


def matching_table(request):
    return render(request, 'configurator/matching_table.html')


def assembly_pc(request):
    return render(request, 'configurator/assembly_pc.html')