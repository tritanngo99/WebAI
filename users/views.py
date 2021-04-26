import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        print('login 11')
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('/')
        else:
            message = 'Login failed'

    return render(request, 'users/login.html', {'message': message})


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
    pattern = '[a-zA-Z0-9]{4,64}'
    if len(password)<8:
        return 'Mat khau it nhat 8 ki tu'
    if password != re_password:
        return 'Nhập lại mật khẩu không trùng khớp'
    dem=0
    for t in password:
        if(48 <=ord(t) and ord(t)<=57 ):
            dem+=1
    if(dem==len(password)):
        return  'Mat khau phai chua it nhat 1 ki tu khac so'
    # elif not re.match(pattern, password):
    #     return 'Mật khẩu phải có 4 kí tự trở lên'
    return None
