from typing import Iterable, Optional

from django.contrib.auth import get_user_model
from django.db import models

TASK_STATUS_CHOICES = [
    ('N', 'NEW'),
    ('I', 'IN PROGRESS'),
    ('P', 'IN PAUSE'),
    ('D', 'DONE'),
]

TASK_PRIORITY_CHOICES = [
    ('HH', 'Highest'),
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
    ('LL', 'Lowest'),
]

User = get_user_model()


class Task(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(choices=TASK_STATUS_CHOICES, max_length=2)
    priority = models.CharField(
        choices=TASK_PRIORITY_CHOICES, default='M')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
