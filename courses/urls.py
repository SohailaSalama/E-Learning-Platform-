from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('create/', views.course_create, name='course_create'),
    path('<int:course_id>/enroll/', views.course_enroll, name='course_enroll'),
    path('assignment/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
    path('submission/<int:submission_id>/grade/', views.grade_assignment, name='grade_assignment'),
    path('assignments/', views.assignment_list, name='assignment_list'),
]

