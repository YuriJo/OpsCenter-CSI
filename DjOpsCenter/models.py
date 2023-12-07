from django.db import models

class Commands(models.Model):
    name = models.CharField(max_length=100)
    command_text = models.CharField(max_length=200)

    def __str__(self):
        return self.name

from django.db import models

class Clients(models.Model):
    unique_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
