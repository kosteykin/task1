from django.db import models


class Records(models.Model):
    client = models.CharField(max_length=30)
    phone_number = models.TextField()
    status = models.CharField(max_length=30)
    price = models.FloatField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.client
