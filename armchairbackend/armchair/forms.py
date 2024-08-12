from django import forms
from armchair.models import Document

# build a form from the document model
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document']