from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import User


@receiver(post_save, sender=User)
def university_post_save(sender, **kwargs):
    instance = kwargs.get('instance')
    created = kwargs.get('created')
    if created and instance.is_university == True:
        message ="""
        Your university {instance.university_name} is successfully registered.
        
        username: {instance.username}
        
        Regard,
        UNISOO
        """
        instance.send_mail(
            'University Registered',
            message,
            'unisoo@gmail.com',
            instance.email
        )
