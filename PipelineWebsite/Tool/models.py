# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FileModel(models.Model):
    FirstName = models.CharField(max_length=30,default="")
    LastName = models.CharField(max_length=30,default="")
    Email = models.EmailField()
    TumorFile = models.FileField()
    NormalFile = models.FileField()
    def __str__(self):
        return str(self.FirstName + "'s project")