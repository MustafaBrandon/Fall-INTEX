from django.shortcuts import render
from django.http import HttpResponse
from CSIapp.models import *


# Create your views here.
def indexPageView(request) :
    return render(request, 'CSIapp/index.html')

def drugdetailsPageView(request) :
    return render(request, 'CSIapp/drugdetails.html')