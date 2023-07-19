from django.contrib import admin
from .models import Blog,Comment, UpDown, BlogView,Category

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(UpDown)
admin.site.register(BlogView)
admin.site.register(Category)
