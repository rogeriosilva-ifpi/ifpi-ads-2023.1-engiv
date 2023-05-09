from django.urls import path

from .views import HelloView, ListTaskView

urlspatterns = [
    path('hello', HelloView.as_view(), name='hello'),
    path('ping', HelloView.as_view(), name='ping_pong'),

    # Tasks
    path('tasks', ListTaskView.as_view(), name='tasks-list')
]
