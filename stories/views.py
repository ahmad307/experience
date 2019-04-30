from django.shortcuts import render, HttpResponse
from stories.models import (
    add_category,
    add_article,
    add_user,
    delete_user,
    user_valid,
    get_user_data,
    add_session,
    get_session_email,
    get_session_username)


def home(request):
    return render(request, 'stories/login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'stories/registration.html')

    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if add_user(name, email, password):
        return render(request, 'stories/login.html',
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
        session_id = add_session(email)
        data = get_user_data(email)
        data.update({'session_id': session_id})
        return render(request, 'stories/profile.html', data)
    else:
        return render(request, 'stories/login.html',
                      {'response_message': 'Login Failed.'})


def create_article(request):
    """
    Creates an article or redirects to create article page.
    :param request: GET, redirects to create_article template
    :param request: POST, adds the new article to database.
    :return: None
    """
    if request.method == 'GET':
        user_name = get_session_username(request.GET['session_id'])
        data = {'user_name': user_name, 'session_id': request.GET['session_id']}
        return render(request, 'stories/new_article.html', data)

    email = get_session_email(request.POST['session_id'])
    add_article(
        request.POST['title'],
        request.POST['body'],
        request.POST['category'],
        request.POST['topic'],
        email)

    return HttpResponse('Article Created.')
