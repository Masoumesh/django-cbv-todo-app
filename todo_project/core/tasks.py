# core/tasks.py
from celery import shared_task
from core.models import Task  
@shared_task
def delete_completed_tasks():
    completed_tasks = Task.objects.filter(is_done=True)
    deleted_count, _ = completed_tasks.delete()
    print(f"Deleted {deleted_count} completed tasks")
    return f"Deleted {deleted_count} completed tasks"