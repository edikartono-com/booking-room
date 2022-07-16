from django.urls import path

from customer import views

app_name = 'customer'

urlpatterns = [
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('', views.Dashboard.as_view(), name='dashboard')
]