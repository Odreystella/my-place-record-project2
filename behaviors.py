from django.db import models
import time

class BaseField(models.Model):
    created_at = models.TextField(default=time.time())
    updated_at = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True