from django.conf.urls import url
from First_WebApp import views


urlpatterns = [
    url('hp', views.home, name="Home Page"),
    url('test', views.index, name="index"),
]