from celery import shared_task
from .models import Task
import requests
from django.core.cache import cache
from django.conf import settings

@shared_task
def delete_completed_tasks():
    Task.objects.filter(is_done=True).delete()
    

    
def fetch_weather():
    city = "Tehran" 
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cache.set("weather_data", data, timeout=60 * 60)  # an hour cache
        print("Weather data cached.")
        return "Weather data cached."
    else:
        print("Failed to fetch weather data.")
        return "Failed to fetch weather data."
