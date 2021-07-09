from django.shortcuts import render ,redirect
from . models import Product
# Create your views here.


def display(request,username = None):
    return render(request,'product/views.html',{
            'username':username
        })


def search(request,username = None):
    if request.method == "POST":
        categary = ["seeds", "seed","fertilizers","fertilisers","pestisides","manures","fertilzer","fertiliser","pestiside","manure"]
        search_value = request.POST.search
        if search_value.lower() in categary:
            if username != None:
                url = f"{username}/product/{search_value}"
            else:
                url = f"product/{search_value}"
            return redirect(request,url,{
                'username':username,
            })

        products = Product.objects.all().filter(name = search_value.lower())
        return render(request,'product/search.html',{
            'products':products
        })



def seeds(request,username = None ,seedname=None):
    if seedname ==None:
        seeds = Product.objects.all().filter(category = 'seeds')
        return render(request, 'product/seeds.html',{
            'seeds': seeds
            })
    else:
        seeds = Product.objects.all().filter(name = seedname)
        return render(request, 'product/seeds.html',{
            'seeds': seeds
        })


def fertilizers(request,username = None ,fertilizername=None):
    if fertilizername ==None:
        fertilizers = Product.objects.all().filter(category = 'fertilizers')
        return render(request, 'product/fertilizers.html',{
            'fertilizers': fertilizers
            })
    else:
        fertilizers = Product.objects.all().filter(name = fertilizername)
        return render(request, 'product/fertilizers.html',{
            'fertilizers': fertilizers
        })


def pestisides(request,username = None ,pestisidename=None):
    if pestisidename ==None:
        pestisides = Product.objects.all().filter(category = 'pestisides')
        return render(request, 'product/pestisides.html',{
            'pestisides': pestisides
            })
    else:
        pestisides = Product.objects.all().filter(name = pestisidename)
        return render(request, 'product/pestisides.html',{
            'pestisides': pestisides
        })

def manures(request,username = None ,manurename=None):
    if manurename ==None:
        manures = Product.objects.all().filter(category = 'manures')
        return render(request, 'product/manures.html',{
            'manures': manures
            })
    else:
        manures = Product.objects.all().filter(name = manurename)
        return render(request, 'product/manures.html',{
            'manures': manures
        })


