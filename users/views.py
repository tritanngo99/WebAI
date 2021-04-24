import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

    return render(request, 'users/login.html', {})


def register(request):
    message = ''
    if request.method == 'POST':
        user, error = get_user(request)
        if user is not None:
            redirect('/login')
        else:
            message = error

    return render(request, 'users/register.html', {'message': message})


def get_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    re_password = request.POST.get('re_password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    error = check_username(username)
    if error is not None:
        return None, error

    error = check_password(password, re_password)
    if error is not None:
        return None, error

    user = User(username=username, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return user, None


def check_username(username):
    pattern = '[a-zA-Z0-9]{4,64}'
    if not re.match(pattern, username):
        return 'Username phải có 4 kí tự trở lên'
    elif User.objects.filter(username=username).exists():
        return 'Username đã tồn tại'
    else:
        return None


def check_password(password, re_password):
    pattern = '[a-zA-Z0-9]{4,64}'
    if password != re_password:
        return 'Nhập lại mật khẩu không trùng khớp'
    elif re.match(pattern, password):
        return 'Username phải có 4 kí tự trở lên'
    return None
