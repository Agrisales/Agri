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
        search_value = request.POST['search']
        if search_value.lower() in categary:
            if username != None:
                url = f"/{username}/product/{search_value}"
            else:
                url = f"/product/{search_value}"
            return redirect(url)
        
        if username:
            products = Product.objects.all().filter(id = search_value.lower())
            return render(request,'product/search.html',{
                'products':products,
                'username':username
            })

        else:
            products = Product.objects.all().filter(id = search_value.lower())
            return render(request,'product/search.html',{
                'products':products
            })



def seeds(request,username = None ):
    if username :
        seeds = Product.objects.all().filter(category = 'seeds')
        return render(request, 'product/seeds.html',{
            'seeds': seeds,
            'username':username
            })
    else:
        seeds = Product.objects.all().filter(category = 'seeds')
        return render(request, 'product/seeds.html',{
            'seeds': seeds,
            })


def fertilizers(request,username = None ):
    if username :
        fertilizers = Product.objects.all().filter(category = 'fertilizers')
        return render(request, 'product/fertilizers.html',{
            'fertilizers': fertilizers,
            'username':username
            })
    else:
        fertilizers = Product.objects.all().filter(category = 'fertilizers')
        return render(request, 'product/fertilizers.html',{
            'fertilizers': fertilizers ,
            })


def pestisides(request,username = None):
    if username :
        pestisides = Product.objects.all().filter(category = 'pestisides')
        return render(request, 'product/pestisides.html',{
            'pestisides': pestisides,
            'username':username
            })
    else:
        pestisides = Product.objects.all().filter(category = 'pestisides')
        return render(request, 'product/pestisides.html',{
            'pestisides': pestisides,
            })

def manures(request,username = None):
    if username :
        manures = Product.objects.all().filter(category = 'manures')
        return render(request, 'product/manures.html',{
            'manures': manures,
            'username':username
            })
    else:
        manures = Product.objects.all().filter(category = 'manures')
        return render(request, 'product/manures.html',{
            'manures': manures,
            })

def view(request,productname,username=None):
    if username:
        product = Product.objects.get(id = productname)
        return render(request,'product/view_product.html',{
        'product':product,
        'username':username
        })
    else:
        product = Product.objects.get(id = productname)
        return render(request,'product/view_product.html',{
        'product':product
    })
