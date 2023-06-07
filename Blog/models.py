from django.db import models
import uuid
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, )
    title = models.CharField(max_length=70)
    description = HTMLField()
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    coverImage = models.ImageField(upload_to='Static/Blogs')
    
    def __str__(self):
        return self.title
