from django.db import models
from django.conf import settings
from django.utils import timezone

time_now = timezone.now

User = settings.AUTH_USER_MODEL
# Create your models here.
class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    active_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.owner.username}'

    def save(self, *args, **kwargs):
        if self.active and self.active_at is None:
            self.active_at = time_now()
        else:
            self.active_at = None
        super().save(*args, **kwargs)
        