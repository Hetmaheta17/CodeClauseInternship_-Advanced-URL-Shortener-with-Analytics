from django.db import models
from django.contrib.auth.models import User

# Shortened URL Model
class ShortenedURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, null=True)
    click_count = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"

# Analytics Model
class Analytics(models.Model):
    shortened_url = models.ForeignKey(ShortenedURL, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"Analytics for {self.shortened_url.short_url} - {self.timestamp}"
