from django.shortcuts import render,redirect

# Create your views here.

def Login(request):
    return render(request,"Login.html")
def Home(request):
    if request.method=="POST":
        
        return render(request,"Home.html")
    else:
        return redirect("/Login/")    