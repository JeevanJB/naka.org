from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#from salesforce import models

# Create your models here.
"""
class SFConnect(models.Model):
    personaldata = models.CharField(max_length=100)
    phonenum = models.IntegerField()

"""
ORG_TYPES = (
    ('household','Household'),
    ('organization', 'Organization'),
)
    
class Contact(models.Model):
    fullname = models.CharField(max_length=50, default = None)
    email  = models.CharField(max_length=50, default = None)
    comment  = models.CharField(max_length=100, default = None)

class Profile(models.Model):
    user = models.OneToOneField(User)
    user_orgtype = models.CharField(max_length=20, choices=ORG_TYPES, default='household')
    user_cellPhone  = models.IntegerField()
    user_homePhone  = models.IntegerField()
    user_address = models.CharField(max_length=200, null=True)
    user_country = models.CharField(max_length=50, null=True)
    user_state = models.CharField(max_length=50, null=True)
    user_city = models.CharField(max_length=50, null=True)
    user_zip  = models.IntegerField()
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""
