from django.shortcuts import render

# Create your views here.

def Login(request):
    return render(request,"/Login.html")
def Home(request):
    return render(request,"/Home.html")