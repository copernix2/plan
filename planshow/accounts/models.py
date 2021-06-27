from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

# Create your models here.

PROFILE_CHOICES = (('icp', 'Infirmier chef de poste'), ('plan', 'Staff Plan'),('xxx', 'xx'))

class Profil(models.Model):
    # id = models.AutoField(primary_key=True) 
    poste = models.CharField(primary_key=True, max_length=45, blank=True)
    district = models.CharField(max_length=45, blank=True, null=True)
    region=  models.CharField(max_length=45, blank=True, null=True)
    logo = models.CharField(max_length=45, blank=True, null=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)
    profile = models.CharField(choices=PROFILE_CHOICES, max_length=255,blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profil')

    def __str__(self) :
        return str(self.user)

    class Meta:
        db_table = 'accounts_profil'
