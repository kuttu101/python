from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1> this is our home page </h1>')

def about(request):
    return HttpResponse('<h1> this is our about us page with all info about us </h1>')

def contact(request):
    return HttpResponse('<h1> this is our contact page where you can reach out to us</h1>')
