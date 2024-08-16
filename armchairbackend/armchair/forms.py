from django import forms
from armchair.models import Document

# build a form from the document model
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Document
        # all fields
        fields = ['user', 'document']
        required = ['user', 'document']