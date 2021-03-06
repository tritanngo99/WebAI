import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.core.handlers.wsgi import WSGIRequest


def sign_out(request: WSGIRequest):
    logout(request)
    return redirect('/')


def login(request: WSGIRequest):
    message = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            redirect_to = '/'

            if request.POST.get('next') != '':
                redirect_to = request.POST.get('next')

            return redirect(redirect_to)
        else:
            message = 'Login failed'

    return render(request, 'users/login.html', {'message': message})


def register(request: WSGIRequest):
    message = ''
    if request.method == 'POST':
        user, error = get_user(request)
        if user is not None:
            return redirect('/login')
        else:
            message = error

    return render(request, 'users/register.html', {'message': message})


def get_user(request: WSGIRequest):
    username = request.POST.get('username')
    password = request.POST.get('password')
    re_password = request.POST.get('re_password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')

    error = check_username(username)
    if error is not None:
        return None, error

    error = check_password(password, re_password)
    if error is not None:
        return None, error

    user = User(username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.set_password(password)
    user.save()
    return user, None


def check_username(username):
    pattern = '[a-zA-Z0-9]{4,64}'
    if not re.match(pattern, username):
        return 'Username ph???i c?? 4 k?? t??? tr??? l??n'
    elif User.objects.filter(username=username).exists():
        return 'Username ???? t???n t???i'
    else:
        return None


def check_password(password, re_password):
    if len(password) < 8:
        return 'M???t kh???u ??t nh???t 8 k?? t???'
    if password != re_password:
        return 'Nh???p l???i m???t kh???u kh??ng tr??ng kh???p'

    number_pattern = '^[0-9]+$'
    if re.match(number_pattern, password):
        return 'M???t kh???u ph???i ch???a m???t k?? t??? kh??c s???'

    character_pattern = '^[a-zA-Z0-9]+$'
    if not re.match(character_pattern, password):
        return 'M???t kh???u ch??? ???????c ch???a c??c k?? t??? a-z, A-Z, 0-9'
    return None
