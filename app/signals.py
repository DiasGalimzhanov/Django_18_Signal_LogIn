from django.dispatch import receiver
import os
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from .models import CustomUser

@receiver(pre_delete, sender=CustomUser)
def delete_user_profile(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)
    
pre_delete.connect(delete_user_profile, sender=CustomUser)