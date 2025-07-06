from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home_view(requste: HttpRequest):

    contant = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(contant)


def about_view(requste: HttpRequest):
    contant = "A simple paragraph about Car Rentals."
    return HttpResponse(contant)