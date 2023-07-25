from django.contrib import admin
from .models import Blog,Comment, UpDown, BlogView,Category


admin.site.register(Comment)
admin.site.register(UpDown)
admin.site.register(BlogView)
admin.site.register(Category)


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
   list_display = ['title', 'slug', 'author', 'is_published', 'categories']
   list_filter = ['is_published', 'datetime', 'categories', 'author']
   search_fields = ['title', 'description']
   prepopulated_fields = {'slug': ('title',)}
   raw_id_fields = ['author']
   date_hierarchy = 'datetime'
   ordering = ['is_published', 'datetime']