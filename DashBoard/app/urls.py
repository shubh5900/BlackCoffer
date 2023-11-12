from django.urls import path, include
from . import views

urlpatterns = [
    path("Login/",views.Login),
    path("Home/",views.Home),
    path("",views.Login),
]
