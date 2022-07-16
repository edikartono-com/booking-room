from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView

from datetime import datetime, timedelta

from customer.forms import RoomBookingForm, CustomerOrderForm
from customer.models import RoomBooking

from manager.cart import Cart
from manager.models import AvailableRooms

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'customer/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        unbooked = AvailableRooms.objects.filter(
            # booking_date_slot__gte = datetime.today(),
            # booking_date_slot__lte = datetime.today() + timedelta(days=30),
            is_booked=False
        )
        date_list = []

        for room in unbooked:
            #if room.booking_date_slot not in date_list:
            date_list.append(room.booking_date_slot)
        
        all_date_slot = AvailableRooms.objects.filter(
            booking_date_slot__gte = datetime.today(),
            booking_date_slot__lte = datetime.today() + timedelta(days=30)
        ).order_by('booking_date_slot')
        full_slot = list(set(all_date_slot) - set(date_list))

        context = super(Dashboard, self).get_context_data(*args, **kwargs)
        context['full_slot'] = full_slot
        context['date_list'] = date_list
        return context

class OrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'customer/order/form.html'
    form_class = CustomerOrderForm
    success_url = reverse_lazy("customer:dashboard")
    success_message = "Room %(booked_room_type)s"

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save(commit=False)
        order.customer = self.request.user
        order.save()

        for item in cart:
            RoomBooking.objects.create(
                customer=order,
                booking_date_slot=item['product']
            )
        cart.clear()
        return super(OrderCreateView, self).form_valid(form)