from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer

from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "core/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description"]
    template_name = "core/task_form.html"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "is_done"]
    template_name = "core/task_form.html"
    success_url = reverse_lazy("task-list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "core/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")


class TaskDoneView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.is_done = True
        task.save()
        return redirect("task-list")
    
    


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed, created, updated, and deleted.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]  # Only logged-in users can access

    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user
        )  # Show only user's tasks

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )  # Assign task to the logged-in user
        
        
        

class WeatherView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        data = cache.get("weather_data")
        if data:
            return Response(data)
        return Response({"error": "Weather data not available."}, status=404)