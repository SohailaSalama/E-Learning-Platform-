"""
URL configuration for e_learningplatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/register/', include('users.urls')),  # Registration and user URLs
    path('users/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # Login
    path('users/dashboard/', include('users.urls')),  # Dashboard or other user actions
    path('courses/', include('courses.urls')),  # Courses app URLs
    path('notifications/', include('notifications.urls')),

    # Add this line to route `/` to the login page
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

