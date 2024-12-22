from django.test import TestCase
from rest_framework.exceptions import ValidationError
from base.serializers import CourseSerializer

class CourseSerializerTest(TestCase):

    def test_valid_course_serializer(self):
        data = {
            'name': 'Test Course',
            'description': 'A description of the test course'
        }

        serializer = CourseSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'Test Course')
        self.assertEqual(serializer.validated_data['description'], 'A description of the test course')

    def test_invalid_course_serializer(self):
        data = {
            'name': '',
            'description': ''
        }
        serializer = CourseSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

