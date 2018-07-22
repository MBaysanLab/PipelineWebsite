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
    return render(request,'AutoTool.html',c)

@require_POST
def upload(request):
    f = forms.UploadForm(request.POST,request.FILES)
    if (f.is_valid()):
        cleaned = f.cleaned_data
        print "First name " + cleaned['FirstName']
        for f in request.FILES.getlist('TumorFile'):
            SaveUploadedFile(f,f.name,"Tumor",cleaned['Email'])
        for f in request.FILES.getlist('NormalFile'):
            SaveUploadedFile(f,f.name,"Normal",cleaned['Email'])
        for f in request.FILES.getlist('PanelOfNormals'):
            SaveUploadedFile(f, f.name, "PanelOfNormals", cleaned['Email'])
    else:
        print "ERROR! IT NEVER WORKED"
    return redirect("/Home")

def SaveUploadedFile(f,fname,directory,email):
    with open('DownloadedFiles/'+directory+'/'+fname,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    #send_mail('Your file has been Processed!', 'Hello! Your file has been processd, here are is the report on every letter in the file:\n' + s
    #         , 'mohammedabunada@std.sehir.edu.tr',
    #          [email], fail_silently=False)