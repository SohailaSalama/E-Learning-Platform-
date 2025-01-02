import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.hashers import make_password
from base.models import User, Course, Assignment

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'password': 'testpassword',
        'email': 'testuser@example.com',
        'name': 'Test User',
        'role': 'student'
    }

@pytest.fixture
def create_user(user_data):
    user = User.objects.create(
        username=user_data['username'],
        email=user_data['email'],
        password=make_password(user_data['password']),
        name=user_data['name'],
        role=user_data['role']
    )
    return user

@pytest.mark.django_db
def test_user_creation(api_client, user_data):
    response = api_client.post(reverse('signup'), user_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_user_login(api_client, create_user, user_data):
    response = api_client.post(reverse('login'), {
        'username': user_data['username'],
        'password': user_data['password']
    }, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'message' in response.data
    assert response.data['message'] == 'Login successful'

@pytest.mark.django_db
def test_course_creation(create_user):
    course_data = {
        'name': 'Test Course',
        'description': 'Test Description',
        'doctor': create_user
    }
    course = Course.objects.create(**course_data)
    assert course.name == 'Test Course'
    assert course.doctor == create_user

@pytest.mark.django_db
def test_assignment_creation(create_user):
    course = Course.objects.create(
        name='Test Course',
        description='Test Description',
        doctor=create_user
    )
    assignment = Assignment.objects.create(
        course=course,
        title='Test Assignment',
        description='Test Description',
        due_date='2024-12-31'
    )
    assert assignment.title == 'Test Assignment'
    assert assignment.course == course

@pytest.mark.django_db
def test_course_list(api_client, create_user):
    api_client.force_authenticate(user=create_user)
    response = api_client.get(reverse('course-list'))
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_assignment_list(api_client, create_user):
    api_client.force_authenticate(user=create_user)
    response = api_client.get(reverse('assignment-list'))
    assert response.status_code == status.HTTP_200_OK