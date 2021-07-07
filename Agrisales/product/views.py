from django.shortcuts import render ,redirect
from . models import Product
# Create your views here.


def display(request,username = None):
    return render(request,'product/views.html',{
            'username':username
        })


def search(request,username = None):
    if request.method == "POST":
        categary = ["seeds","fertilizers","fertilisers","pestisides","manures"]
        search_value = request.POST.search
        if search_value.lower() in categary:
            if username != None:
                url = f"{username}/product/{search_value}"
            else:
                url = f"product/{search_value}"
            return render(request,url,{
                'username':username,
            })

        products = Product.objects.all().filter(name = search_value.lower())
        return render(request,'product/search.html',{
            'products':products
        })



def seeds(request,username = None ,seedname=None):
    if seedname ==None:
        seeds = Product.objects.all()
        return render(request, 'product/seeds.html',{
            'seeds': seeds
            })
    else:
        seeds = Product.objects.all().filter(name = seedname)
        return render(request, 'product/seeds.html',{
            'seeds': seeds
        })



