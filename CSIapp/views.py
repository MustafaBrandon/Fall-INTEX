from django.shortcuts import render
from CSIapp.models import *


# Create your views here.
def indexPageView(request) :
    return render(request, 'CSIapp/index.html')

def drugdetailsPageView(request) :
    return render(request, 'CSIapp/drugdetails.html')

def prescriberdetailsPageView(request) :
    data = Prescriber.objects.all()

    context = {
        "our_prescriber" : data,
    }
    return render(request, 'CSIapp/prescriberdetails.html', context)

def prescribersearchPageView(request):

    prescriber_data = Prescriber.objects.all

    context = {
        "prescribers" : prescriber_data,
    }
    return render(request, 'CSIapp/drugdetails.html',context)