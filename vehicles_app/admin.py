from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(VehicleMakes),
admin.site.register(VehicleModels),
admin.site.register(Vehicles),
admin.site.register(Defects),
admin.site.register(Contacts),
admin.site.register(ServiceBookings),
admin.site.register(Parts),
admin.site.register(PartsOrderList),

