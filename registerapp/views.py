from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Users
# Create your views here.
def register(request):
    if(request.method=="POST"):
        username = request.POST['name']
        password=request.POST['password']
        ph_no=request.POST['phone']
        add=request.POST["address"]
        try:
            user = User.objects.create_user(username=username,password=password)
            user.save()
            m=Users.objects.create(user_n=user,phone_no=ph_no,address=add)
            m.save()
            return redirect("login")
        except:
            return render(request,"Register.html") 
        
    else:
        return render(request,"Register.html") 