from django.urls import path
from . import views
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDoneView


urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('new/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/done/', TaskDoneView.as_view(), name='task-done'),
]