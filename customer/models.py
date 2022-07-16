from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from manager.models import AvailableRooms, RoomTypes

class Customers(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    other = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user_id.get_full_name)

class CustomersOrder(models.Model):
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    customer_name = models.CharField(_("Nama pelanggan"),max_length=60, help_text="Nama atau Perusahaan/Organisasi")
    booking_purpose = models.CharField(_("Keperluan"), max_length=254, help_text="Tujuan booking ruangan ini")
    start_time = models.TimeField(_("Waktu mulai"))
    end_time = models.TimeField(_("Waktu selesai"))
    #coupon
    #discount
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.id}"

class RoomBooking(models.Model):
    customer = models.ForeignKey(
        CustomersOrder,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='customer_booking'
    )
    booking_date_slot = models.OneToOneField(
        AvailableRooms,
        on_delete=models.PROTECT,
        related_name='booked_date'
    )
    booked_room_type = models.ForeignKey(
        RoomTypes,
        on_delete=models.PROTECT,
        related_name='booked_room'
    )    

    def __str__(self):
        return self.customer