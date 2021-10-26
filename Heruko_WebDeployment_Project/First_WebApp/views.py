from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    dir_name = {'insert_me': "Hello Labhesh in Consultadd Inc" }
    return render(request,'First_WebApp\HomePage.html', context = dir_name)


