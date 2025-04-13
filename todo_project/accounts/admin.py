from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "bio",
        "is_staff",
    ]
    list_filter = ["is_staff", "is_superuser"]
    search_fields = ["username", "email"]
    ordering = ["username"]


admin.site.register(CustomUser, CustomUserAdmin)
