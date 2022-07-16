from django import forms
from django.forms import ModelForm

from customer.models import RoomBooking, CustomersOrder

class RoomBookingForm(ModelForm):
    class Meta:
        model = RoomBooking
        fields = '__all__'

class CustomerOrderForm(ModelForm):
    class Meta:
        model = CustomersOrder
        # fields = '__all__'
        exclude = ['customer']