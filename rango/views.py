from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! Here is a link to the about page <br/><a href='/rango/about/'>About</a>")
	
def about(request):
	return HttpResponse("Rango says here is the about page with a link to the index page: <br/><a href='/rango/'>Index</a>")

