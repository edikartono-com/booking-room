from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.html import strip_tags
from django.utils.text import slugify, Truncator
from manager.models import RoomTypes
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='dashboard/')

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.full_name

class Featured(models.Model):
    name = models.OneToOneField(RoomTypes, on_delete=models.CASCADE, related_name='featured')
    desc = models.TextField()

class Facilities(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=150, help_text='User font awesome icon, eg. fas fa-chalkboard')
    desc = RichTextField(verbose_name="Description")
    img = models.ImageField(upload_to="facilities/", verbose_name="Image")
    start_hour = models.TimeField(help_text="Start service hours")
    end_hour = models.TimeField(help_text="End service hours")
    
    def __str__(self):
        return self.name

class BlogCategories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True)
    visible_menu = models.BooleanField(default=True)

    class Meta:
        ordering = ['-name']

    def save(self):
        if self.slug == None:
            self.slug = slugify(self.name)
        super(BlogCategories, self).save()
    
    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse('dash:category', kwargs={'slug': self.slug})

def blog_image(instance, filename):
    return "blog/{0}/{1}".format(instance.category, filename)

class Blog(models.Model):
    title = models.CharField(max_length=180, unique=True)
    summary = models.TextField(blank=True, null=True)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to=blog_image)
    category = models.ForeignKey(
        BlogCategories,
        to_field='slug',
        on_delete=models.PROTECT,
        related_name='blog_category'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='user_blog'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering = ['-created_at']
    
    def strip_body(self):
        bory = strip_tags(self.body)
        trucn_bory = Truncator(bory).chars(170)
        return trucn_bory
    
    def save(self, *args, **kwargs):
        if self.slug == None:
            self.slug = slugify(self.title)
        self.summary = self.strip_body()
        super(Blog, self).save(*args, **kwargs)
    
    def get_image(self):
        if self.image:
            return self.image.url
    
    def get_absolute_url(self):
        return reverse_lazy('dash:blog_detail', kwargs={'cat': self.category, 'slug': self.slug})
    
    def __str__(self):
        return "{0} by {1}".format(self.title, self.author)

class Services(models.Model):
    icon = models.CharField(
        max_length=50,
        help_text='''icon name only. e.g: ti-alarm-clock <br> more icon : <a href="https://themify.me/themify-icons" target="_blank" rel="noopener">themify icons</a>'''
    )
    service = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.service