from django.db import models
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError

from datetime import date, timedelta

class RoomTypes(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.name

# class DateAndSlot(models.Model):
#     booking_date = models.DateField()
#     rooms_type = models.ForeignKey(RoomTypes, on_delete=models.SET_NULL, blank=True, null=True)
#     rooms_add = models.BooleanField(default=False)

#     class Meta:
#         unique_together = ('booking_date', 'rooms_type')
    
#     def save(self, *args, **kwargs):
#         if self.booking_date < date.today():
#             raise ValidationError("Date must be in future")
#         super(DateAndSlot, self).save(*args, **kwargs)
    
#     def handle(self, *args, **options):
#         self.objects.filter(booking_date - timedelta(days=1)).delete()
#         self.stdout.write('Deleted object older than 10 days')
    
#     def __str__(self):
#         return "Date : {0} \n Type : {1}".format(self.booking_date, self.rooms_type)

class AvailableRooms(models.Model):
    booking_date_slot = models.DateField()
    type_available = models.ForeignKey(RoomTypes, on_delete=models.PROTECT)
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('booking_date_slot', 'type_available')
    
    def save(self, *args, **kwargs):
        if self.booking_date_slot < date.today():
            raise ValidationError("Date must be in future")
        super(AvailableRooms, self).save(*args, **kwargs)
    
    def handle(self, *args, **options):
        self.objects.filter(self.booking_date_slot - timedelta(days=1)).delete()
        self.stdout.write('Deleted object older than 10 days')

    def __str__(self):
        return "Booking Date : {0} Type : {1}".format(
            self.booking_date_slot,
            self.type_available.name
        )

# class Room(models.Model):
#     chosen_date_slot = models.ForeignKey(DateAndSlot, on_delete=models.CASCADE)
#     chosen_room_type = models.ForeignKey(RoomTypes, on_delete=models.CASCADE)
#     is_booked = models.BooleanField(default=False)

#     def __str__(self):
#         return "Date {0} Type: {1}".format(self.chosen_date_slot, self.chosen_room_type)