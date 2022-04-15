from django.shortcuts import render


def dashboard(request):
    return render(request, 'base/dashboard.html')


def about(request):
    return render(request, 'base/about.html')