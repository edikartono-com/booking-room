from django.urls import path

from dashboard import views

app_name = 'dash'

urlpatterns = [
    path('services/', views.ServicesList.as_view(), name='services'),

    path('blog/<str:cat>/<slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('blog/<slug>/', views.CategoryList.as_view(), name='category'),
    path('blog/', views.BlogList.as_view(), name='blog_list'),

    path('check/availability/room/', views.RoomAvailableView.as_view(), name='check_room'),
    path('search/<str:q>/', views.BlogSearch.as_view(), name='search'),
    path('', views.HomePage.as_view(), name='home'),
]