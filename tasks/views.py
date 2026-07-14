from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    Standard CRUD for tasks. Supports basic filtering via query params
    (?status=pending, ?priority=high) handled in get_queryset.
    """

    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status_param = self.request.query_params.get("status")
        priority_param = self.request.query_params.get("priority")
        if status_param:
            queryset = queryset.filter(status=status_param)
        if priority_param:
            queryset = queryset.filter(priority=priority_param)
        return queryset
