from django.db import models


class Key(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    value = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.value
