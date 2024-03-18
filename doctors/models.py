from django.db import models
from users.models import User
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)    
    degree = models.CharField(max_length=100, blank=True, null=True)
    #experience = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    fees = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
