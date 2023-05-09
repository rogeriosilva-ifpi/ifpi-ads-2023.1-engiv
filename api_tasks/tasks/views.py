from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer


class ListTaskView(APIView):

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class HelloView(APIView):

    def get(self, request):
        data = {'message': 'Hello DJ+DRF'}
        return Response(data)

    def post(self, request):
        name = request.data.get('name') or 'Rogério'
        return Response({"pong": name})
