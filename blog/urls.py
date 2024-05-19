from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post', views.add_post, name='add_post'),
    path('post_detial/<str:slug>/', views.post_detail, name='post_detail'),
     path('post_detial/<str:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
     path('post_detial/<str:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('edit_post/<int:post_id>',
         views.post_edit, name='post_edit'),
    path('post_delete/<int:post_id>',
         views.post_delete, name='post_delete'),
     path('like/<slug:slug>', views.post_like,
          name='post_like'),
     path('unlike/<slug:slug>', views.post_unlike,
          name='post_unlike'),
    
    
    
]