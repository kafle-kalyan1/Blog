from django.contrib import admin
from .models import Blog
# from tinymce.widgets import TinyMCE
# from Blog import models


# class BlogAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': TinyMCE()},
#     }


admin.site.register(Blog)
