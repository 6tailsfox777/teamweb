from django.db import models

class SensorReading(models.Model):
    value = models.FloatField(verbose_name="感測器數值")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="記錄時間")

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.timestamp} - {self.value}"