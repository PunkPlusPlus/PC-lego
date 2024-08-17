from django.shortcuts import render


def components(request):
    return render(request, 'parser/components.html')


def matching_table(request):
    return render(request, 'parser/matching_table.html')


def source(request):
    return render(request, 'parser/source.html')