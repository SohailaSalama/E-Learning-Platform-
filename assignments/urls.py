from django.urls import path
from . import views

urlpatterns = [
    path('submit/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('grade/<int:submission_id>/', views.grade_assignment, name='grade_assignment'),
]
