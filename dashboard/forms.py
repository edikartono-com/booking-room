from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Facilities, Blog

class FacilitiesForm(ModelForm):
    class Meta:
        model = Facilities
        fields = '__all__'

    def clean_img(self):
        image = self.cleaned_data.get('img', False)
        if image:
            big = float(image.size / 1024000)
            if image.size > 1*1024*1024:
                raise ValidationError("Max file size is 1MB, your image %.2f MB" % big)
            return image
        else:
            raise ValidationError("please select image!")

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'summary', 'body', 'image', 'category']
    
    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            big = float(image.size / 1024000)
            if image.size > 1*1024*1024:
                raise ValidationError("Max file size is 1MB, your image %.2f MB" % big)
            return image
        else:
            raise ValidationError("please select image!")