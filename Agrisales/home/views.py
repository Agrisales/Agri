from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def userhome(request, username):
    return render(request, 'home/userhome.html', {
        'username': username
    })
