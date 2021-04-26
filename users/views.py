import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout


def sign_out(request):
    logout(request)
    return redirect('/')


def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            message = 'Login failed'

    return render(request, 'users/login.html', {'message': message})


def register(request):
    message = ''
    if request.method == 'POST':
        user, error = get_user(request)
        if user is not None:
            return redirect('/login')
        else:
            message = error

    return render(request, 'users/register.html', {'message': message})


def get_user(request):
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
        return 'Username phải có 4 kí tự trở lên'
    elif User.objects.filter(username=username).exists():
        return 'Username đã tồn tại'
    else:
        return None


def check_password(password, re_password):
    if len(password) < 8:
        return 'Mật khẩu ít nhất 8 kí tự'
    if password != re_password:
        return 'Nhập lại mật khẩu không trùng khớp'

    number_pattern = '^[0-9]+$'
    if re.match(number_pattern, password):
        return 'Mật khẩu phải chứa một kí tự khác số'

    character_pattern = '^[a-zA-Z0-9]+$'
    if not re.match(character_pattern, password):
        return 'Mật khẩu chỉ được chứa các kí tự a-z, A-Z, 0-9'
    return None
