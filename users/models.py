from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#=============Notes================
#!dont forget constraints
#!dont forget th img field
#!dont forget the serializer
#==================================
class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    phone = models.CharField(max_length=5, blank=True, null=True)
    # yousef 3ayz yeshelha
    age = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,default='M')
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    



class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)    
    degree = models.CharField(max_length=100, blank=True, null=True)
    #experience = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
#rating    
class Rating(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  
