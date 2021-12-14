from django.urls import path, include
from .views import DriverList, DriverDetail, VehicleList, VehicleDetail


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('drivers/driver/', DriverList.as_view()),
    path('drivers/driver/<int:pk>/', DriverDetail.as_view()),
    path('vehicles/vehicle/', VehicleList.as_view()),
    path('vehicles/vehicle/<int:pk>/', VehicleDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
