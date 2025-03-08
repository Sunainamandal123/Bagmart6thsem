from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator

# Create your models here.
class UserProfile (models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    password =models.CharField(max_length=30)
    
class Product(models.Model):
    image = models.ImageField(upload_to='images/', blank=False, null=False, default='images/default.jpg')
    name = models.CharField(max_length=200, null= False , blank= False)
    price = models.DecimalField(max_digits=10, decimal_places=3 ,  validators=[MinValueValidator(0.001)])
    description=models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  
     
     # different thau mah product insert garnulai 
    is_featured = models.BooleanField(default=False)  
    is_new = models.BooleanField(default=False) 
     
    def __str__(self):
        return self.name
    
from django.db import models
from django.core.validators import MinValueValidator

class Bag(models.Model):
    CATEGORY_CHOICES = [
        ('Shoulder Bag', 'Shoulder Bag'),
        ('Luggage', 'Luggage'),
        ('Duffle', 'Duffle'),
        ('Purse', 'Purse'),
        ('Others', 'Others'),
    ]

    image = models.ImageField(upload_to='images/', blank=False, null=False, default='images/default.jpg')
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(0.001)])
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Others')  # Added category field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
