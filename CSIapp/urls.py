from django.urls import path
#all of the views
from .views import *


urlpatterns = [
    #path("about/", aboutPageView, name="about"),
    path("",indexPageView,name="index"),
    path("drugdetails/", drugdetailsPageView, name="drugdetails"),

    path("searchprescriber/", prescribersearchPageView, name="prescribersearch"), 

]

