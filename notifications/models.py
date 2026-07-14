from django.db import models

from tasks.models import Task


class NotificationLog(models.Model):
    CHANNEL_CHOICES = [
        ("email", "Email"),
        ("sms", "SMS"),
    ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    channel = models.CharField(max_length=10, choices=CHANNEL_CHOICES, default="email")
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.channel}] {self.message}"
