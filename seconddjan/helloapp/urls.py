from django.urls import path
from helloapp import views

urlpatterns = [
    path("", views.home, name="home"),

]