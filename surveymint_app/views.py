from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This home page")

def signup(request):
    return HttpResponse("This works for SignUp")






