from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.notifications_view, name='notifications'),
    path('notifications/<int:notification_id>/mark_as_read/', views.mark_as_read, name='mark_as_read'),
      path('', views.notifications_list, name='notifications_list'),
]
