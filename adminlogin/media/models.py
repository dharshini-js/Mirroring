from django.db import models

class Store_media(models.Model):
    photo_urls = models.URLField(blank=True, null=True)
    video_urls = models.URLField(blank=True, null=True)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Media ({self.photo_urls}, {self.video_urls})"
