from symbol import parameters
from turtle import RawTurtle
from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Tags,Elements,purchases
from django.urls import reverse
# from .models import Items
# Create your views here.
def main(request):
    if request.method=="GET":
        if request.user.is_authenticated and not request.user.is_superuser:
            content=[]
            tags=Tags.objects.all().values_list('section', flat=True)
            elements=Elements.objects.all()
            for i in tags:
                content.append({i:elements.filter(typee=i)})
            return render(request,"Main.html",{"contents":content})
        else:
            return redirect("home")
    else:
        namee=request.POST["name"]  
        price=request.POST["price"]  
        image=request.POST["image"]
        request.session["name"]=namee
        request.session["price"]=price
        request.session["image"]=image
        # d={"name":namee,"price":price,"image":image}
        # return HttpResponseRedirect("product",d)
        return redirect("prod")
def productt(request):
    if(request.method=="GET"):
        namee=request.session.get("name")
        price=request.session.get("price")
        image=request.session.get("image")
        d={"name":namee,"price":price,"image":image}
        return render(request,"product.html",d)
    else:
        total=request.POST.get('total', False)
        quantity=request.POST.get('quantity', False)
        request.session["total"]=total
        request.session["quantity"]=quantity
        return redirect("bill")
        
def bill(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        namee=request.session.get("name")
        total=request.session.get("total")
        quantity=request.session.get("quantity")
        current_user = request.user
        p=purchases.objects.create(user_n=current_user,product_name=namee,quantity=quantity,total=total)
        p.save()
        d={"name":namee,"total":total,"quantity":quantity}
        return render(request,"bill.html",d)
def pay(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        total=request.session.get("total")
        d={"total":total}
        return render(request,"pay.html",d)