from django.db import models
from django.contrib.auth.models import User
# Built in signals
# from django.db.models.signals import post_save
# # decorators for signal receivers
# from django.dispatch import receiver

# Create your models here.
# User extension info
class Profile(models.Model):
    # one to one relationship with the user model
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    # phone number field
    phone = models.CharField(max_length=20, blank=True)
    # Profile Pic
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    # Personal profile
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return 'User {} '.format(self.user.username)

# # signal receiving function, automatically called whenever a USer instance is created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# def save_user_profile(sender, instance, **kwargs):
#     instance.Profile.save()