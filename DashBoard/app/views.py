from django.shortcuts import render,redirect

# Create your views here.

def Login(request):
    print(request.method=="POST")
    if request.method=="POST":
        return redirect("/Home/")
    else:
        return render(request,"Login.html")
def Home(request):
    
    return render(request,"Home.html")