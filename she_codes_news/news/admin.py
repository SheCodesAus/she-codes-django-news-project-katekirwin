from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.NewsStory)

admin.site.register(models.Comment)