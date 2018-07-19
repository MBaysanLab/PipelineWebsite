# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def Main(request):
    return render(request,'HomePage.html')

def ToolSelection(request):
    return render(request,'ToolSelection.html')