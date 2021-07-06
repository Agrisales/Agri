from django.urls import path
from . import views

urlpatterns = [
    path('/seeds',views.seeds,name= "seeds"),
    path('/seeds/<str:seedname>', views.seeds, name="seedview"),
    path('',views.display,name="display")
]