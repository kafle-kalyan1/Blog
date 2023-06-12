from django.urls import path
from . import views




urlpatterns = [
    path('', views.blog, name='blog'),
    path('search',views.search_view, name='search'),
    path('id/<str:id>', views.blogPost,name="blogPost" ),
    path('handleComment', views.handleComment, name='handleComment'),
    path('upvote_comment', views.upvote_comment, name='upvote_comment'),
    path('downvote_comment', views.downvote_comment, name='downvote_comment'),
    

]

