from models import FileModel
from django import forms

class UploadForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['FirstName','LastName','Email','TumorFile','NormalFile']