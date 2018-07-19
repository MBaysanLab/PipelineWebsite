# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from . import forms
def Main(request):
    return render(request,'HomePage.html')

def ToolSelection(request):
    return render(request,'ToolSelection.html')

def AutomaticToolSelect(request):
    c={'form':forms.UploadForm}
    return render(request,'AutomaticTool.html',c)

@require_POST
def upload(request):
    f = forms.UploadForm(request.POST,request.FILES)
    if (f.is_valid()):
        cleaned = f.cleaned_data
        print cleaned['FirstName']
    return redirect("/Home")