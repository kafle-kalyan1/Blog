from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.blog, name='blog'),
    path('search',views.search_view, name='search'),
    path('<str:id>', views.blogPost, ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # adding static 

