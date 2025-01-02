from django.db import models
from django.conf import settings
from courses.models import Course



class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE,  # Use CASCADE or another appropriate deletion behavior
        related_name="assignments"  # Optional, allows reverse access from Course
    )

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'courses_course'  # Keep the original database table name
        managed = True


class Submission(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assignment_submissions'
    )
    graded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='graded_assignment_submissions'
    )
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Submission by {self.student} for {self.assignment}"
    
    class Meta:
        db_table = 'courses_course'  # Keep the original database table name
        managed = True
