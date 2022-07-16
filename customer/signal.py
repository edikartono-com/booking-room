from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from customer.models import Customers

@receiver(post_save, sender=User)
def after_user_created(sender, instance, created, **kwargs):
    if created:
        Customers.objects.create(user_id=instance)