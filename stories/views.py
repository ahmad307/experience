from django.shortcuts import render, HttpResponse
from stories.models import (
    add_category,
    add_article,
    add_user,
    delete_user,
    user_valid)


def home(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'registration.html')

    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    add_user(name, email, password)
    return HttpResponse('Registered!')


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if user_valid(email, password):
        return HttpResponse('Logged In')
    else:
        return HttpResponse('Login Failed.')
