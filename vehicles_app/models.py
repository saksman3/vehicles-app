from django.db import models
serviceType=(('MAJOR','major'),
             ('NORMAL','normal'),
             ('minor','MINOR'),
            )
# Create your models here.
class VehicleModels(models.Model):
      modelDescription = models.CharField(max_length=255)

      def __str__(self):
          return self.modelDescription

class VehicleMakes(models.Model):
      makeDescription = models.CharField(max_length=255)
      def __str__(self):
          return self.makeDescription
class Vehicles(models.Model):
      serialNumber = models.AutoField(primary_key=True)
      makeCode = models.ForeignKey(VehicleMakes,on_delete=models.CASCADE)
      modelCode = models.ForeignKey(VehicleModels,on_delete=models.CASCADE)

class Defects(models.Model):
      serialNumber = models.ForeignKey(Vehicles,on_delete=models.CASCADE)
      defect_desc = models.CharField(max_length=255)
      def __str__(self):
          return self.defect_desc

class Contacts(models.Model):
      contactID = models.AutoField(primary_key=True)
      contactName = models.CharField(max_length=255)
      def __str__(self):
          return self.contactName

class ServiceBookings(models.Model):
      serialNumber = models.ForeignKey(Vehicles,on_delete=models.CASCADE)
      contactID = models.ForeignKey(Contacts,on_delete=models.CASCADE)
      serviceType = models.CharField(choices=serviceType, max_length=255, default='Normal')

      """  def __str__(self):
          serial = Vehicles.objects.get(pk=self.serialNumber_id)
          return str(serial)+' - '+self.serviceType"""

class Parts(models.Model):
      partDesc = models.CharField(max_length=255)
      def __str__(self):
          return self.partDesc
class PartsOrderList(models.Model):
      serialNumber = models.ForeignKey(ServiceBookings,on_delete=models.CASCADE)
      partID = models.ForeignKey(Parts,on_delete=models.CASCADE)
