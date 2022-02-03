from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import inventory, customer, rentalBooking
from django.contrib import messages

#Home Page
def index(request):
    return render(request, 'base.html')

def addCustomer(request):
    if request.method == 'POST':
        customerName = request.POST.get('cName')
        email = request.POST.get('email')
        phoneno = request.POST.get('phone')
        Customer = customer(customerName = customerName, phoneno = phoneno, email = email)
        Customer.save()
        messages.info(request,'customer added successfully!')
    return render(request, 'addCustomer.html')

def addRental(request):
    customerlist = customer.objects.all()
    inventories = inventory.objects.all()
    context = {'customerlist':customerlist, 'inventories':inventories}
    if request.method == 'POST':
        customerName = request.POST.get('cName')
        rentalDate = request.POST.get('rdate')
        returnDate = request.POST.get('rndate')
        vehicle = request.POST.get('vehicle')
        if returnDate == "":
            returnDate = None
        list = inventory.objects.get(vehicleType = vehicle)
        if list.available > 0:
            list.available -= 1
            list.save()
            Rent = rentalBooking(customerName = customerName, rentalDate = rentalDate, returnDate = returnDate, vehicleType = vehicle)
            Rent.save()
            messages.info(request,'Ordere Placed successfully!')
            return render(request, 'addRental.html',context)
        else:
            context = {'customerlist':customerlist, 'inventories':inventories, 'vehicle':vehicle}
            messages.info(request,', cannot be rented as it is already booked')
            return render(request, 'addRental.html',context)
    return render(request, 'addRental.html',context)

def seeCustomer(request):
    customerlist = customer.objects.all()

    return render(request, 'seeCustomer.html', {"customerlist":customerlist})

def seeInventory(request):
    inventories = inventory.objects.all()
    return render(request, 'seeInventory.html',{"inventories":inventories})

def seeRental(request):
    bookings = rentalBooking.objects.all()
    return render(request, 'seeRental.html', {"bookings":bookings})