from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

#this model stores the data of the Phones verified
class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    username = models.CharField(max_length=255)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    
    def __str__(self):
        return str(self.Mobile)