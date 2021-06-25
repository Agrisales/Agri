from django.shortcuts import redirect, render
from django.contrib.auth import logout
from login.models import User
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def userhome(request, username):
    return render(request, 'home/userhome.html', {
        'username': username
    })


def userprofile(request, username):
    current_user = request.user
    user = User.object.get(pk=current_user.phone_number)
    return render(request, 'home/userprofile.html', {
        'username': user.user_name,
        'phonenumber': user.phone_number,
        'datejoined': user.date_joined,
        'email': user.email
    })
