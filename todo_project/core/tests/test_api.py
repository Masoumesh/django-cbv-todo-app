import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Task
from accounts.models import CustomUser


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return CustomUser.objects.create_user(username='testuser', password='testpass123')


@pytest.fixture
def auth_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def task(user):
    return Task.objects.create(title="Sample Task", description="Test Desc", user=user)


def test_get_task_list(auth_client, task):
    url = reverse("task-list")
    response = auth_client.get("/api/tasks/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["title"] == "Sample Task"


def test_create_task(auth_client):
    data = {"title": "New Task", "description": "New Desc"}
    response = auth_client.post("/api/tasks/", data)
    assert response.status_code == 201
    assert response.data["title"] == "New Task"


def test_update_task(auth_client, task):
    url = f"/api/tasks/{task.id}/"
    data = {"title": "Updated Task", "description": "Updated Desc", "is_done": True}
    response = auth_client.put(url, data)
    assert response.status_code == 200
    assert response.data["title"] == "Updated Task"
    assert response.data["is_done"] is True


def test_delete_task(auth_client, task):
    url = f"/api/tasks/{task.id}/"
    response = auth_client.delete(url)
    assert response.status_code == 204
    assert Task.objects.count() == 0
