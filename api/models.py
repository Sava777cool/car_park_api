from django.db import models
from django.utils import timezone


class Driver(models.Model):
    '''The driver model describes the basic information about the driver.
      You can specify the created_at date yourself. The updated_at date is updated automatically.'''
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''The function returns the driver's name for easy display in the admin panel.'''
        return self.first_name


class Vehicle(models.Model):

    '''The car model is linked to the driver via driver_id.
    The driver_id field can be null.
    You can specify the created_at date yourself. The updated_at date is updated automatically.'''

    id = models.IntegerField(primary_key=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    make = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    plate_number = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''The function returns the model of the car for the convenience of displaying in the admin panel.'''
        return self.model
