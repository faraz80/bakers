from django.urls import path
from . import views
urlpatterns = [
    path("",views.main,name="main"),
    path("prod/",views.productt,name="prod"),
    path("bill/",views.bill,name="bill"),
    path("payy/",views.pay,name="pay")
]