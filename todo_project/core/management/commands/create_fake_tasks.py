from django.core.management.base import BaseCommand
from core.models import Task
from faker import Faker
import random
from django.contrib.auth import get_user_model

fake = Faker()
User = get_user_model()

class Command(BaseCommand):
    help = 'Create 5 fake tasks with random completion status for each user'

    def handle(self, *args, **kwargs):
        users = User.objects.all()

        if not users.exists():
            self.stdout.write(self.style.ERROR('❌ No users found. Please create users first.'))
            return

        for user in users:
            for _ in range(5):
                Task.objects.create(
                    title=fake.sentence(nb_words=4),
                    description=fake.text(max_nb_chars=200),
                    is_done=random.choice([True, False]),
                    user=user
                )
            self.stdout.write(self.style.SUCCESS(f'{user.username}'))

        self.stdout.write(self.style.SUCCESS('done!'))
