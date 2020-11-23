from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    content = models.CharField(max_length=512, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.content
