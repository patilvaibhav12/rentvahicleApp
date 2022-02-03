from django.contrib import admin
from .models import inventory, customer, rentalBooking
# Register your models here.
admin.site.register(inventory)
admin.site.register(customer)
admin.site.register(rentalBooking)