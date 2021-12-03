from django.shortcuts import render
from django.http import HttpResponse
from CSIapp.models import *


# Create your views here.
def indexPageView(request) :
    return render(request, 'CSIapp/index.html')

def drugdetailsPageView(request) :
    return render(request, 'CSIapp/drugdetails.html')

def prescriberdetailsPageView(request) :
    return render(request, 'CSIapp/prescriberdetails.html')

def prescribersearchPageView(request):
    data = Prescriber.objects.all()

    context = {
        "our_prescriber" : data,
    }
    return render(request, 'CSIapp/drugdetails.html', context)
