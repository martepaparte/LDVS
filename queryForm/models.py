from django.db import models


class RequestQuery(models.Model):
    formTitle = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

