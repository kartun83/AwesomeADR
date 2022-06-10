from django.db import models

# Create your models here.

class Status(models.Model):
    description = models.TextField()

class System(models.Model):
    createdAt = models.DateTimeField('date created'),
    name      = models.TextField()

class ADR(models.Model):
    createdAt = models.DateTimeField('date published')
    context  = models.TextField(),
    status   = models.ForeignKey(Status, on_delete=models.PROTECT),
    decision = models.TextField(),
    effects  = models.TextField(),  
    affects  = models.ForeignKey(System, on_delete=models.PROTECT)  
    projectLink = models.TextField()