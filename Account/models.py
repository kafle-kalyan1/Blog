from django.db import models

#importing user from auth config
from django.contrib.auth.models import User

class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE )
   profilePic = models.ImageField(null=True, blank=True,  max_length=255)
   bio = models.TextField(null=True, blank=True)
   dob = models.DateField(null=True, blank=True)
   
   def __str__(self):
      return self.user.username
   
