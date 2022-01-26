from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

#this model stores the data of the Phones verified
class phoneModel(models.Model):
    Mobile = PhoneNumberField(blank=True)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    
    def __str__(self):
        return str(self.Mobile)