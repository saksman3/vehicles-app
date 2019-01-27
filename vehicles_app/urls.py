from rest_framework import routers
from django.conf.urls import url, include
from . import views
router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet,base_name="user")
router.register(r'make',views.VehicleMakesViewSet,base_name="make")
router.register(r'model',views.VehicleModelViewSet,base_name="models")
router.register(r'all',views.VehiclesViewSet,base_name="vehicles")
router.register(r'defects',views.DefectsViewSet,base_name="defects")
router.register(r'service',views.ServiceBookingsViewSet,base_name="service")
router.register(r'contacts',views.ContactsViewSet,base_name="contacts")
router.register(r'parts',views.PartsViewSet,base_name="parts")
router.register(r'orderList',views.PartsOrderViewSet,base_name="orderList")
app_name = 'vehicles_app'

urlpatterns = [
                  url(r'^',include(router.urls)),

                  #url(r'^filter/$',views.Filter, name='filter'),
            ]
