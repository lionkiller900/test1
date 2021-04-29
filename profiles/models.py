from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=60, null=True, blank=True)
    default_home_Address = models.CharField(max_length=60, null=True, blank=True)
    default_home_Address_continued = models.CharField(max_length=60, null=True, blank=True)
    default_postcode = models.CharField(max_length=30, null=True, blank=True)
    default_county = models.CharField(max_length=50, null=True, blank=True)
    default_country = CountryField(blank_label='', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def make_or_edit_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()