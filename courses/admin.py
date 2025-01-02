from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'teacher')
    search_fields = ('title', 'teacher__username')
