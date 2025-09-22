from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'pages/home.html')

def carlist(req):
    return render(req, 'pages/carlist.html')

def myinven(req):
    return render(req, 'pages/myinven.html')

def addcar(req):
    return render(req, 'pages/addcar.html')

def sellerprof(req):
    return render(req, 'pages/sellerprof.html')

def dealerD(req):
    return render(req, 'pages/dealerD.html')

def mistake(req):
    return render(req, 'pages/mistake.html')

def bloglist(req):
    return render(req, 'pages/bloglist.html')

def blogdet(req):
    return render(req, 'pages/blogdet.html')

def contactus(req):
    return render(req, 'pages/contactus.html')
