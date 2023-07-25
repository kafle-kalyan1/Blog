from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from django.utils import timezone



class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=150, default="General")
    def __str__(self):
        return self.category
    

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    description = RichTextField()
    datetime = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    coverImage = CloudinaryField('image')
    is_published = models.BooleanField(default=False)
    categories = models.OneToOneField(Category, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-datetime']
        indexes = [
        models.Index(fields=['-datetime']),
        ]


    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user.username} on Blog #{self.blog.id}'

class BlogView(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

class UpDown(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.BooleanField(default=False)
    downvotes = models.BooleanField(default=False)
    
