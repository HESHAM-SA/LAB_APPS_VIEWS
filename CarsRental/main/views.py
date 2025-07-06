from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string

# Create your views here.
def home_view(request : HttpRequest):

    contant = "Hello World, This is my new HOME for Car Rentals Website  ! we're excited to welcome you here."
    return HttpResponse(contant)


def about_view(request : HttpRequest):
    contant = "A simple paragraph about Car Rentals."
    return HttpResponse(contant)

def gen_password(request : HttpRequest):
    numbers = random.sample(string.digits, 2)
    upper = random.sample(string.ascii_uppercase, 3)
    lower = random.sample(string.ascii_lowercase, 3)
    symbols = random.sample(string.punctuation, 2)
    password = numbers + upper + lower + symbols
    random.shuffle(password)
    shuffle_password = ''.join(password)
    return HttpResponse(shuffle_password)



    
