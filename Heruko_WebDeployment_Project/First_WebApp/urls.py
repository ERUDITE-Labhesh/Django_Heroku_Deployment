from django.conf.urls import url
from First_WebApp import views


urlpatterns = [
    url(r'^$', views.home, name = " Home Page"),
]