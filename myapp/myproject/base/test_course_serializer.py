from django.test import TestCase
from api.serializers import CourseSerializer
from base.models import User

class CourseSerializerTest(TestCase):
    def test_course_serializer_valid(self):
        # Create a user (doctor) instance for the course's doctor field
        doctor = User.objects.create(name="Dr. Smith", email="drsmith@example.com", role="doctor")

        # Add the doctor field to the data
        data = {
            'name': 'Test Course',
            'description': 'A test course',
            'doctor': doctor.id  # Assuming doctor is a ForeignKey to User
        }

        # Initialize the serializer with the data
        serializer = CourseSerializer(data=data)

        # Check if the serializer is valid
        self.assertTrue(serializer.is_valid())

        # Optionally, check the validated data
        validated_data = serializer.validated_data
        self.assertEqual(validated_data['name'], 'Test Course')
        self.assertEqual(validated_data['description'], 'A test course')
        self.assertEqual(validated_data['doctor'], doctor)
