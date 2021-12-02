from django.shortcuts import render
from CSIapp.models import *


# Create your views here.
def indexPageView(request) :
    return render(request, 'CSIapp/index.html')

def drugdetailsPageView(request) :
    return render(request, 'CSIapp/drugdetails.html')

def perscriberdetailsPageView(request) :
    return render(request, 'CSIapp/perscriberdetails.html')

def prescribersearchPageView(request):
    prescriber_data = Prescriber.objects.all

    context = {
        "prescribers" : prescriber_data,
    }
    return render(request, 'CSIapp/drugdetails.html',context)
