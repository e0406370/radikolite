from django.db import models


class Radio(models.Model):
    radio_name = models.CharField(max_length=64)
    radio_logo = models.URLField(max_length=128, blank=True, null=True)
    radio_stream = models.URLField(max_length=128)

    def __str__(self):
        return f"Radio: {self.radio_name}, Logo: {self.radio_logo}, Stream: {self.radio_stream}"
