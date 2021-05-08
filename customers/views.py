from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer, Agent
from .forms import CustomerForm, CustomerModelForm

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

def customer_create(request):
    print(request.POST)
    form = CustomerModelForm()
    if request.method == "POST":
        print("Receiving a post request")
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/customers")
    context = {
        "form": CustomerModelForm()
    }
    return render(request, "customers/customer_create.html", context)


def customer_update(request, pk):
     customer = Customer.objects.get(id=pk)
     form = CustomerModelForm(instance=customer)
     if request.method == "POST":
        print("Receiving a post request")
        form = CustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("/customers")
     context = {
       "customer": customer,
       "form": form 
    }
    
     return render(request, 'customers/customer_update.html', context)


def customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete() 
    return redirect("/customers")