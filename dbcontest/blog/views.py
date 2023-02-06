from django.shortcuts import render
from .models import Products
from .models import Customers


def Products_view(request):
    products = Products.objects.all()
    return render(request, 'products_index.html',{'products':products})

def Customers_view(request):
    customers = Customers.objects.all()
    return render(request, 'customer_index.html',{'customers':customers})