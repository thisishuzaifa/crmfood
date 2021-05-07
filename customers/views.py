from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()    
    context = { 
        "customers" : customers,
    }
    return render(request, "customers/customer_list.html", context) 

def customer_detail(request, pk):
  
    customer = Customer.objects.get(id=pk)
    context = {
       "customer": customer 
    }
    return render(request, "customers/customer_details.html", context) 