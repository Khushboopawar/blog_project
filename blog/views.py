from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    home_html="<h1>welcome to home page</>"
    return HttpResponse(home_html)
def about(request):
    home_html="<h1>welcome to about page</>"
    return HttpResponse(home_html)



# Create your views here.
