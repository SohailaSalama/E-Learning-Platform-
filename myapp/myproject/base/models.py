from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=10, null=False, default='student')  # Roles like 'student', 'doctor', 'admin'
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)  # Details about the course
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'enrollments'
        unique_together = ('student', 'course')

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)  # Details about the assignment
    due_date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'assignments'

    def __str__(self):
        return self.title

class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades')
    grade = models.DecimalField(max_digits=5, decimal_places=2)  # Grade up to 2 decimal points
    graded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grades'
        unique_together = ('assignment', 'student')
