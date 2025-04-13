from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import register_user

urlpatterns = [
    path('register/', register_user, name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh
]