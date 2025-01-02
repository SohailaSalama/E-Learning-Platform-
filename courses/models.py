from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Submission(models.Model):
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    submitted_at = models.DateTimeField()
    graded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,  # Use CASCADE or appropriate deletion behavior
        blank=True, 
        null=True
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="submissions"  # Adjust related_name to avoid conflicts
    )

    def __str__(self):
        return f"Submission by {self.student.username}"
    
    class Meta:
        db_table = 'courses_course'  # Keep the original database table name
        managed = True

    



class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'courses_course'  # Keep the original database table name
        managed = True

