from rest_framework import serializers
from base.serializers import CourseSerializer

# Define a simple test case for CourseSerializer
class CourseSerializerTest(TestCase):
    def test_course_serializer_valid(self):
        data = {
            'name': 'Django for Beginners',
            'description': 'Learn Django from scratch',
        }
        
        serializer = CourseSerializer(data=data)
        self.assertTrue(serializer.is_valid())
    
    def test_course_serializer_invalid(self):
        # Missing required field 'name'
        data = {
            'description': 'Learn Django from scratch',
        }
        
        serializer = CourseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)


