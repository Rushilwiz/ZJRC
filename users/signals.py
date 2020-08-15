from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#from social_auth.signals import socialauth_registered


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print ("CREATED")
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print ("SAVED")
    instance.profile.save()
