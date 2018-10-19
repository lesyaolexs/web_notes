from django.db import models
from django.utils import timezone


class Note(models.Model):
    text = models.CharField(max_length=120)
    created = models.DateTimeField(default=timezone.now)
    unique_words = models.IntegerField()

    def __str__(self):
        return self.text

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.unique_words = len(set(self.text.split()))
        super().save(force_insert, force_update, using, update_fields)


