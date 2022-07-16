from django.contrib import admin

from datetime import datetime

from manager.models import AvailableRooms, RoomTypes

admin.site.register(RoomTypes)

@admin.register(AvailableRooms)
class AvailableRoomAdmin(admin.ModelAdmin):
    model = AvailableRooms
    exclude = ['is_booked']

    def render_change_form(self, request, context, *args, **kwargs):
        date_and_slot = AvailableRooms.objects.filter(
            booking_date_slot__gte = datetime.today(),
            #booking_date_slot__lte = datetime.today() + timedelta(days=1)
        )
        context['adminform'].form.fields['booking_date_slot'].queryset = date_and_slot
        return super(AvailableRoomAdmin, self).render_change_form(request, context, *args, **kwargs)