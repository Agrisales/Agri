from django.shortcuts import render

# Create your views here.
def seeds(request,username = None ,seedname=None):
    if seedname ==None:
        return render(request, 'product/seeds.html')
    else:
        return render(request, 'product/seeds.html',{
            'seedname': seedname,
        })

def display(request,username = None):
    if username == None:
        return render(request,'product/views.html')
    else:
        return render(request,'product/views.html',{
            'username':username
        })