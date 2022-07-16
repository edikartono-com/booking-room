from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView

# from customer.models import RoomBooking
from manager.cart import Cart
from manager.forms import CartAddProductForm
from manager.models import AvailableRooms, RoomTypes

class ManagerDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'manager/dashboard.html'

# class AddSlot(LoginRequiredMixin, SuccessMessageMixin, PermissionRequiredMixin, CreateView):
#     #model = DateAndSlot
#     permission_required = ['manager.add_dateandslot']
#     form_class = DateSlotForm
#     success_message = "Slot add sucessfully!"
#     success_url = reverse_lazy('manager:dashboard')
#     template_name = 'manager/manage/form.html'

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(AvailableRooms, id=product_id)
    #form = CartAddProductForm(request.POST)

    if product:
        cart.add(
            product=product
        )
        messages.add_message(request, messages.SUCCESS, 'Masuk keranjang')
    return redirect('manager:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(AvailableRooms, id=product_id)
    cart.remove(product)
    messages.add_message(request, messages.WARNING, 'Product dikeluarkan dari keranjang')
    return redirect('manager:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'override': True
            }
        )
    # coupon next -->
    return render(request, 'manager/cart/detail.html', {'cart': cart})