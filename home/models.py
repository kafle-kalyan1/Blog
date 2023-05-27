from datetime import datetime

from django.db import models

# Create your models here.
class ContactData(models.Model):
    conID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    description = models.TextField()
    phone = models.CharField(max_length=20)
    dateTime = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
