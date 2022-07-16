from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', include('customer.urls')),
    path('accounts/', include('allauth.urls')),
    path('manager/', include('manager.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('dashboard.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)