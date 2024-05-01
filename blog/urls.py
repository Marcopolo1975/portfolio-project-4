from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post', views.post, name='post'),

    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_post/<int:post_id>',
         views.post_edit, name='post_edit'),
     path('<slug:slug>/delete_post/<int:post_id>',
         views.post_delete, name='post_delete'),
     path('like/<slug:slug>', views.like_post.as_view(),
          name='postlikes'),
    
    
    
]