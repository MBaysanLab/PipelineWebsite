from django.conf.urls import url, include
from django.contrib import admin
from views import *
urlpatterns = [
    url(r'^Home/$',Main,name="Home"),
    url(r'^Tool/$', AutomaticToolSelect),
    url(r'^Tool/Automatic/$',AutomaticToolSelect),
    url(r'^Tool/Automatic/Upload$',upload,name="upload")
]
