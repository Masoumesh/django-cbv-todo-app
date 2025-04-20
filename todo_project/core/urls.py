from django.urls import path, include
from . import views
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDoneView,
)


from rest_framework.routers import DefaultRouter
from .views import TaskViewSet


router = DefaultRouter()
router.register(r"api/tasks", TaskViewSet, basename="task")


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("new/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/done/", TaskDoneView.as_view(), name="task-done"),
    path("", include(router.urls)),
    path("weather/", WeatherView.as_view(), name="weather"),
]
