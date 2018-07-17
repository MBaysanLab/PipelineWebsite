# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FileModel(models.Model):
    Email = models.EmailField()
    File = models.FileField()
    def __str__(self):
        return str(self.Email)