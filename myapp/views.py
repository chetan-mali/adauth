from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/microsoft") 
def index(request):
    return HttpResponse("Hello World")

# Create your views here.