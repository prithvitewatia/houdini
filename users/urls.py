from django.urls import path
from .views import settings, profile

urlpatterns = [
    path('profile/<str:username>/', profile, name='users-profile'),
    path('settings/', settings, name='users-settings')
]
