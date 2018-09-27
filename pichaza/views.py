from django.shortcuts import render
from django.http  import HttpResponse
from .models import *


# Create your views here.
def welcome(request):
    return render(request, 'index.html')

# Create your views here.
