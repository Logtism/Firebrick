from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person


def get_view(request):
    return render(request, 'tests_test/get_view.html')


def get_or_404(request, id):
    item = get_object_or_404(Person, id=id)

    return render(request, 'tests_test/get_or_404.html', {'item': item})


@login_required
def login_view(request):
    return render(request, 'tests_test/login_view.html')