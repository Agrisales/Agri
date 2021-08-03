from django.shortcuts import redirect, render
from django.contrib.auth import logout
from login.models import User
# Create your views here.


def home(request):
    if request.user == None:
        return render(request, 'home/home.html')
    else:
        logout(request)
        return render(request, 'home/home.html')


def userhome(request, username):
    current_user = request.user
    user = User.object.get(pk=current_user.phone_number)
    id = user.is_admin
    if id:
        return render(request, 'home/userhome.html', {
        'username': username,
        'admin':True
        })

    return render(request, 'home/userhome.html', {
        'username': username
    })


def userprofile(request, username):
    current_user = request.user
    user = User.object.get(pk=current_user.phone_number)
    return render(request, 'home/userprofile.html', {
        'current_user':current_user,
        'username': user.user_name,
        'phonenumber': user.phone_number,
        'datejoined': user.date_joined,
        'email': user.email,
        'address': user.address,
    })

def cart(request,username):
    return render(request,'home/cart_layout.html',{
        'username':username
    })
