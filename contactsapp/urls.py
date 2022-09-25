from django.urls import path
from . import views
urlpatterns = [
    path("",views.contactt,name="contact"),
]