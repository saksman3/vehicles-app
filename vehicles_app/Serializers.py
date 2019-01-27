from rest_framework import serializers

from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
      url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:user-detail")
      class Meta:
          model = User
          fields = ('url','username','email','is_staff')

class VehicleMakesSerializer(serializers.HyperlinkedModelSerializer):
      url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:make-detail")
      class Meta:
          model = VehicleMakes
          fields = ('id','makeDescription','url')

class VehicleModelsSerializer(serializers.HyperlinkedModelSerializer):
      url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:models-detail")
      class Meta:
          model = VehicleModels
          fields = ('id','modelDescription','url')

class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
      #url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:vehiclemakes-list")
      #url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:vehicles-detail")
      makeCode = VehicleMakesSerializer(many=False,read_only=True)
      modelCode = VehicleModelsSerializer(many=False,read_only=True)
      class Meta:
          model = Vehicles
          fields = ('serialNumber','makeCode','modelCode')

class DefectsSerializer(serializers.HyperlinkedModelSerializer):
      url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:defects-detail")
      class Meta:
          model = Defects
          fields = ('serialNumber','defect_desc','url')

class ServiceBookingsSerializer(serializers.HyperlinkedModelSerializer):
      url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:service-detail")
      class Meta:
          model = ServiceBookings
          fields = ('SerialNumber','ContactID','serviceType','url')

class ContactsSerializer(serializers.HyperlinkedModelSerializer):
      url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:contacts-detail")
      class Meta:
          model = Contacts
          fields = ('contactID','contactName','url')

class PartsSerializer(serializers.HyperlinkedModelSerializer):
      url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:parts-detail")
      class Meta:
          model = Parts
          fields = ('id','partDesc','url')

class PartsOrderListSerializer(serializers.HyperlinkedModelSerializer):
      url = serializers.HyperlinkedIdentityField(view_name="vehicles_app:orderList-detail")

      partID=PartsSerializer(
        many=False,
        read_only=True,
         )
      bookingID=ServiceBookingsSerializer(
                 many=False,
                 read_only=True,
                  )
      class Meta:
          model = PartsOrderList
          fields = ('partID','bookingID','url')
