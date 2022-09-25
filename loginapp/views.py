from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
# Create your views here.
def loginn(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        print(request.user)
        return redirect("main")
    else:
        if(request.method=="GET"):
            return render(request,"Login.html")
        else:
            username=request.POST["name"]
            password=request.POST["password"]
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect("main")
            else:
                return render(request,"Login.html")
