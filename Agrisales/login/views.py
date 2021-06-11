from django.shortcuts import render
from .models import User, UserManager
from .authen import Myauth

# Create your views here.


def login(request):
    if request.method == "POST":

        phone_number = request.POST["phone_number"]
        password = request.POST["password"]
        author = Myauth()
        author.authenticate(
            phone_number=phone_number, password=password)
        if author:
            return render(request, 'login/index.html', {
                "message": "Logged in"
            })
        else:
            return render(request, 'login/index.html', {
                "message": "Wrong Credantials"
            })

    else:
        return render(request, 'login/index.html')


def signup(request):
    if request.method == "POST":
        user__name = request.POST["user_name"]
        phone__number = request.POST["phone_number"]
        emai_l = request.POST["email"]
        pass_word = request.POST["password"]
        pswd_check = request.POST["pswd_check"]
        if pass_word == pswd_check:
            user = User.object.create_user(user_name=user__name, phone_number=phone__number,
                                           email=emai_l, password=pass_word)

            return render(request, 'login/index.html', {
                "message": "Signed up"
            })
    else:
        return render(request, 'login/index.html')
