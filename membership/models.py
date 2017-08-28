from django.db import models

# Create your models here.
class Membership(models.Model):
    #REGISTRATION
    user_fullname  = models.CharField(max_length=50)
    user_profession = models.CharField(max_length=50)
    user_speciality = models.CharField(max_length=50)
    user_alumniOf  = models.CharField(max_length=50, null=True)
    spouse_fullname  = models.CharField(max_length=50, null=True)
    spouse_profession = models.CharField(max_length=50, null=True)
    spouse_speciality = models.CharField(max_length=50, null=True)
    spouse_alumniOf  = models.CharField(max_length=50, null=True)
    user_cellPhone  = models.IntegerField()
    user_homePhone  = models.IntegerField()
    user_address = models.CharField(max_length=200, null=True)
    user_country = models.CharField(max_length=50, null=True)
    user_state = models.CharField(max_length=50, null=True)
    user_city = models.CharField(max_length=50, null=True)
    user_zip  = models.IntegerField()
    #DIRECTORY PREFERENCE
    user_hometown = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    interests = models.CharField(max_length=50, null=True)
    events = models.BooleanField(default=False)
    community_service = models.BooleanField(default=False)
    team_square = models.BooleanField(default=False)
    language_literature = models.BooleanField(default=False)
    sports_arts = models.BooleanField(default=False)
    foundation = models.BooleanField(default=False)
    womens_support = models.BooleanField(default=False)
    spiritual = models.BooleanField(default=False)
