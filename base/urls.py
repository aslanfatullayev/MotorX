from django.urls import path
from .views import home, carlist, myinven, addcar, sellerprof, dealerD, mistake, bloglist, blogdet, contactus

urlpatterns = [
    path ('', home, name ='home'),
    path ('carlist/', carlist, name='carlist'),
    path ('myinven/', myinven, name='myinven'),
    path ('addcar/', addcar, name='addcar'),
    path ('sellerprof/', sellerprof, name='sellerprof'),
    path ('dealerD/', dealerD, name= 'dealerD'),
    path ('mistake/', mistake, name = 'mistake'),
    path ('bloglist/', bloglist, name = 'bloglist'),
    path ('blogdet/', blogdet, name = 'blogdet'),
    path ('contactus/', contactus, name = 'contactus')
]
