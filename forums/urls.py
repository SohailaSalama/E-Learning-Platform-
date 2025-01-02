from django.urls import path
from . import views

urlpatterns = [
    path('<int:forum_id>/', views.forum_view, name='forum_detail'),  # Forum page
    path('<int:forum_id>/post/create/', views.post_create, name='post_create'),  # Post creation page
]
