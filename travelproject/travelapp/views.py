from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, contactteam


# Create your views here.
# def demo(request):
#     name="india"
#     return render(request,'home.html',{'obj1':name})
def index(request):
    obj=Place.objects.all
    cobj=contactteam.objects.all
    return render(request,'index.html',{'res':obj,'cres':cobj})
def result(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,'result.html',{'result':res})
def address(request):
    return render(request,'address.html')
def contact(request):
    return render(request,'contact.html')
def destinations(request):
    return render(request,'destinations.html')
def elements(request):
    return render(request,'elements.html')
def news(request):
    return render(request,'news.html')