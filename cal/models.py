from django.db import models
from django.contrib.auth.models import User

class Calculation(models.Model):
    expression = models.CharField(max_length=200)
    result = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
