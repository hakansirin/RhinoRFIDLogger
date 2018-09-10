from django.db import models

class Log(models.Model):
    reader_id = models.CharField(max_length=128)
    tag_id = models.CharField(max_length=128)
    creation_date = models.DateTimeField(auto_now_add=True)