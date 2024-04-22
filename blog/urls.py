from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     path('addpost/', views.AddPost.as_view(), name='add_post'),
      path(
        'posts/<slug:slug>/delete/',
        views.DeletePost.as_view(), name='delete_post'
        ),
]