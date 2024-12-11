from django.db import models

class Media(models.Model):
    photo_url = models.URLField(max_length=2000, blank=True, null=True)
    video_url = models.URLField(max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Media ({self.photo_url}, {self.video_url})"
