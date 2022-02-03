from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addCustomer/', views.addCustomer, name='addCustomer'),
    path('addRental/', views.addRental, name='addRental'),
    path('seeCustomer/', views.seeCustomer, name='seeCustomer'),
    path('seeRental/', views.seeRental, name='seeRental'),
    path('seeInventory/', views.seeInventory, name='seeInventory'),
]