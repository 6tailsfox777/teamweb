from django.db import models
from django.utils import timezone


class SensorReading(models.Model):
    topic = models.CharField(max_length=255)
    sensor_name = models.CharField(max_length=100)
    value = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=50, blank=True)
    raw_payload = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp", "-created_at"]

    def __str__(self):
        return f"{self.sensor_name} ({self.value})"
