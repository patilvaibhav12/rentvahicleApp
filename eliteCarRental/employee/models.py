from django.db import models


class inventory(models.Model):
    vehicleType = models.CharField(max_length=100)
    available = models.IntegerField()

    def __str__(self):
        return self.vehicleType

class customer(models.Model):
    customerName = models.CharField(max_length=150)
    phoneno = models.IntegerField()
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.customerName

class rentalBooking(models.Model):
    customerName = models.CharField(max_length=150)
    rentalDate = models.DateField(blank=True)
    returnDate = models.DateField(blank=True, null=True)
    vehicleType = models.CharField(max_length=150)
    
    def __str__(self):
        return self.customerName
