
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

# for weather
weather_schedule, _ = IntervalSchedule.objects.get_or_create(every=20, period=IntervalSchedule.MINUTES)

task_name = "fetch-weather-every-20-minutes"
task, created = PeriodicTask.objects.get_or_create(
    name=task_name,
    defaults={
        "interval": weather_schedule,
        "task": "core.tasks.fetch_weather",
        "kwargs": json.dumps({}),
    },
)
if not created:
    task.interval = weather_schedule
    task.task = "core.tasks.fetch_weather"
    task.save()
    print(f"Updated periodic task {task_name}")
else:
    print(f"Successfully created periodic task {task_name}")
