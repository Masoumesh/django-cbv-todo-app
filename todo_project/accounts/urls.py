from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_user, UserProfileView


urlpatterns = [
    path("register/", register_user, name="register"),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # JWT login
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # JWT refresh
    path("profile/", UserProfileView.as_view(), name="user_profile"),
]
