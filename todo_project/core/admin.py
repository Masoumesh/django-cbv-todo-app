from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "is_done",
        "created_date",
        "updated_date",
    )


admin.site.register(Task, TaskAdmin)

# Register your models here.
