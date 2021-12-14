from rest_framework import generics
from django_filters import rest_framework as filters
from .serializers import DriverSerializer, VehicleSerializer
from .models import Driver, Vehicle

'''Filtering driver creation by date.'''
class DateFilter(filters.FilterSet):
    '''The gte argument filters after the specified number in Y-m-d format.'''
    created_at__gte = filters.DateTimeFilter(field_name="created_at", lookup_expr='gte')
    '''The lte argument filters before the specified number in Y-m-d format.'''
    created_at__lte = filters.DateTimeFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Driver
        fields = ['created_at']


class DriverList(generics.ListCreateAPIView):
    '''Displaying a list of all drivers. Class complete POST and GET requests.'''
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_class = DateFilter


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Detailed information about each driver. Class complete GET, PUT and DELETE requests.'''
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class VehicleList(generics.ListCreateAPIView):
    '''List of all vehicles. Class complete POST and GET requests.'''
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Detailed information about each vehicle. Class complete GET, PUT and DELETE requests.'''
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


