from django.shortcuts import render, HttpResponse
from stories.models import (
    add_category,
    add_article,
    add_user,
    delete_user,
    user_valid,
    get_user_data)


def home(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'registration.html')

    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if add_user(name, email, password):
        return render(request, 'login.html',
                      {'response_message': 'Successfully Registered.'})
    else:
        return HttpResponse('Email Already Used.')


def login(request):
    """
    Authenticates user and redirects to user profile.
    :return:
        - User profile page if authentication succeeds.
        - Login page with error msg dict.
    """
    email = request.POST['email']
    password = request.POST['password']
    if user_valid(email, password):
        return render(request, 'profile.html', get_user_data(email))
    else:
        return render(request, 'login.html',
                      {'response_message': 'Login Failed.'})


def create_article(request):
    # TODO: Handle create article requests
    if request.method == 'GET':
        return render(request, 'new_article.html', {'user_name': 'Ahmad'})
