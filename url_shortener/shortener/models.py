from django.db import models

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return f"Short URL: {self.short_url} -> {self.original_url}"
