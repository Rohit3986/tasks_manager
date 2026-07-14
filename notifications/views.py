from rest_framework import viewsets

from .models import NotificationLog
from .serializers import NotificationLogSerializer


def send_notification(task, message, channel="email"):
    """
    Sends (mock) a notification and logs it.
    Actual delivery is not implemented - this just creates a log entry.
    """
    return NotificationLog.objects.create(task=task, message=message, channel=channel)


class NotificationLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NotificationLog.objects.all().order_by("-sent_at")
    serializer_class = NotificationLogSerializer
