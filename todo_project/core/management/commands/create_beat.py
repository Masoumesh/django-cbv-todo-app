
from django.core.management.base import BaseCommand

from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

# for weather
class Command(BaseCommand):
    help = "Create or update periodic task to fetch weather"

    def handle(self, *args, **kwargs):
        schedule, _ = IntervalSchedule.objects.get_or_create(
            every=20,
            period=IntervalSchedule.MINUTES,
        )

        PeriodicTask.objects.update_or_create(
            name="fetch-weather-every-20-minutes",
            defaults={
                "interval": schedule,
                "task": "core.tasks.fetch_weather_data",  # Make sure this matches your task
                "args": json.dumps([]),
            }
        )
        self.stdout.write(self.style.SUCCESS("Successfully created periodic task fetch-weather-every-20-minutes"))