from django.urls import path
#all of the views
from .views import *


urlpatterns = [
    #path("about/", aboutPageView, name="about"),
    path("",indexPageView,name="index"),
    path("drugdetails/", drugdetailsPageView, name="drugdetails"),
    path('perscriberdetails/', perscriberdetailsPageView, name="perscriberdetails"),
    path("searchprescriber/", prescribersearchPageView, name="prescribersearch"), 
]

