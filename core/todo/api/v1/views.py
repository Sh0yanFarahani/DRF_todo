from ...models import Todo
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
class TaskViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]