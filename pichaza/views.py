from django.shortcuts import render
from django.http  import HttpResponse
from .models import *


# Create your views here.
def welcome(request):

    images = Image.get_images()
    context={'images': images}
    return render(request, 'index.html', context)

# Create your views here.
