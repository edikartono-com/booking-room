from django.contrib import admin
from customer.models import Customers, CustomersOrder, RoomBooking

admin.site.register(Customers)
admin.site.register(RoomBooking)

class RoomBookingInline(admin.TabularInline):
    model = RoomBooking
    raw_id_fields = ['booking_date_slot']

@admin.register(CustomersOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer_name','created']
    list_filter = ['customer_name','created']
    inlines = [RoomBookingInline]