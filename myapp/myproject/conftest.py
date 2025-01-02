import pytest
from rest_framework.test import APIClient
from django.contrib.auth.hashers import make_password
from base.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'password': 'testpassword', 
        'email': 'test@example.com',
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