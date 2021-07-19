from django.urls import path
from . import views

urlpatterns = [
    path('/seeds',views.seeds,name= "seeds"),
    path('',views.display,name="display"),
    path('/search',views.search, name="search"),
    path('/fertilizers',views.fertilizers,name= "fertilizers"),
    path('/pestisides',views.pestisides,name= "pestisides"),
    path('/manures',views.manures,name= "manures"),
    path('/view/<str:productname>',views.view, name="view")

 
]