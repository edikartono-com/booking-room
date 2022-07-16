from datetime import datetime
from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm

from manager.models import AvailableRooms

# class DateSlotForm(ModelForm):
#     class Meta:
#         model = DateAndSlot
#         fields = ['booking_date', 'rooms_type']

# class AddRoomForm(ModelForm):
#     class Meta:
#         model = AvailableRooms
#         fields  = ['rooms_available']

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 2)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )

    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput()
    )