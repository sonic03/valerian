from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Blog,Cats,CatsType


qs = CatsType.objects.all().values_list('id','title') if CatsType.objects.all().exists() else (0,'Bir kedi seçin')

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content','url','img','is_active','is_mainpage')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': u'Başlık','class':'form-control'}),
            'content': CKEditorWidget(),
            'url': forms.TextInput(attrs={'placeholder': u'Url','class':'form-control'}),

        }

class CatForm(forms.ModelForm):

    class Meta:
        model = Cats
        fields = ('title', 'content','gender','cat_type','img','is_active','is_mainpage')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': u'Başlık','class':'form-control'}),
            'content': CKEditorWidget(),
            'cat_type':forms.Select(choices=qs,attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),

        }
