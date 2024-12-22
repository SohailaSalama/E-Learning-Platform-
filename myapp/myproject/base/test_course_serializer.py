from django.test import TestCase
from base.serializers import CourseSerializer

class CourseSerializerTest(TestCase):
    def test_course_serializer_valid(self):
        data = {
            'name': 'Django for Beginners',
            'description': 'Learn Django from scratch',
        }
        # Create a CourseSerializer instance
        serializer = CourseSerializer(data=data)
        # Check if the serializer is valid
        self.assertTrue(serializer.is_valid())

    def test_course_serializer_invalid(self):
        # Missing required field 'name'
        data = {
            'description': 'Learn Django from scratch',
        }
        serializer = CourseSerializer(data=data)
        # Check if the serializer is invalid and 'name' is a required field
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)


