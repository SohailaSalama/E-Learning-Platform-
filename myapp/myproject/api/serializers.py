from rest_framework import serializers
from base.models import User, Course, Enrollment, Assignment, Grade

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'role', 'created_at']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'doctor', 'created_at', 'updated_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'course', 'title', 'description', 'due_date', 'created_at']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'assignment', 'student', 'grade', 'graded_at']
