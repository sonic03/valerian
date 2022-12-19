from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import About


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ('content',)
        widgets = {
            'content': CKEditorWidget(),
        }
