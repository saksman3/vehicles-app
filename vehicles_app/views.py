from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .Serializers import *
from django.contrib.auth.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VehicleMakesViewSet(viewsets.ModelViewSet):
      queryset = VehicleMakes.objects.all()
      serializer_class = VehicleMakesSerializer

class VehicleModelViewSet(viewsets.ModelViewSet):
      queryset = VehicleModels.objects.all()
      serializer_class = VehicleModelsSerializer

class VehiclesViewSet(viewsets.ModelViewSet):
      queryset = Vehicles.objects.all()
      serializer_class = VehiclesSerializer

class DefectsViewSet(viewsets.ModelViewSet):
      queryset = Defects.objects.all()
      serializer_class = DefectsSerializer

class ServiceBookingsViewSet(viewsets.ModelViewSet):
      queryset = ServiceBookings.objects.all()
      serializer_class = ServiceBookingsSerializer

class ContactsViewSet(viewsets.ModelViewSet):
      queryset = Contacts.objects.all()
      serializer_class = ContactsSerializer

class PartsViewSet(viewsets.ModelViewSet):
      queryset = Parts.objects.all()
      serializer_class = PartsSerializer

class PartsOrderViewSet(viewsets.ModelViewSet):
     queryset =PartsOrderList.objects.all()
     serializer_class = PartsOrderListSerializer       
