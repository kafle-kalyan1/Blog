from django.db import models
import uuid
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=70)
    description = HTMLField()
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    coverImage = models.ImageField(upload_to='static/Blogs')
    
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
