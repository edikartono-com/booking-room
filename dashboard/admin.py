from django.contrib import admin
from dashboard.models import (
    AboutUs, ContactUs, Featured,
    Blog, BlogCategories, Facilities,
    Services
)
from dashboard.forms import BlogForm, FacilitiesForm

admin.site.register(AboutUs)
admin.site.register(ContactUs)
admin.site.register(Featured)
admin.site.register(Services)

@admin.register(BlogCategories)
class BlogCategoriesAdmin(admin.ModelAdmin):
    exclude = ['slug']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm

    def get_form(self, request, *args, **kwargs):
        form = super(BlogAdmin, self).get_form(request, *args, **kwargs)
        #form.author = request.user
        return form
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        return super(BlogAdmin, self).save_model(request, obj, form, change)

@admin.register(Facilities)
class FacilitiesAdmin(admin.ModelAdmin):
    form = FacilitiesForm