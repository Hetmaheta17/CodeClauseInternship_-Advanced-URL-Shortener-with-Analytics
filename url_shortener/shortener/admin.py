from django.contrib import admin
from shortener.models import ShortenedURL,Analytics
# Register your models here.
admin.site.register(ShortenedURL)
admin.site.register(Analytics)