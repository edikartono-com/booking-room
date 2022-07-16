from django.urls import path
from manager import views

app_name = 'manager'

urlpatterns = [
    path('cart/detail/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    # path('add-slot/', views.AddSlot.as_view(), name='addslot'),
    path('', views.ManagerDashboard.as_view(), name='dashboard'),
]