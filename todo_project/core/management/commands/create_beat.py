from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.utils.timezone import now
import random
import string


class Command(BaseCommand):
    help = 'Creates a periodic task that deletes completed tasks every 10 minutes'

    def handle(self, *args, **options):
        # Check if task exists and delete it
        task_name = "delete-completed-tasks-every-10-minutes"
        try:
            task = PeriodicTask.objects.get(name=task_name)
            task.delete()
            self.stdout.write(self.style.SUCCESS(f'Deleted existing periodic task {task_name}'))
        except PeriodicTask.DoesNotExist:
            self.stdout.write(self.style.WARNING(f'Periodic task {task_name} does not exist, skipping deletion'))

        # Create a new task
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.MINUTES,
        )

        # Create the periodic task
        task = PeriodicTask.objects.create(
            name=task_name,
            task='core.tasks.delete_completed_tasks',
            interval=schedule,
            enabled=True,
            last_run_at=now(),
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created periodic task {task_name}'))
