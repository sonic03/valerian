from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class Blog(models.Model):
    title=models.CharField(verbose_name='Başlık',max_length=255)
    content = RichTextField(verbose_name='İçerik')
    url=models.CharField(verbose_name='Url',max_length=999)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(verbose_name='Aktif',default=False)
    is_mainpage = models.BooleanField(verbose_name='Ana Sayfa',default=False)
    img = models.FileField(upload_to='img/')

    def __str__(self):
        return self.title


class CatsType(models.Model):
    title=models.CharField(verbose_name='Kedi Türü',max_length=255)


    def __str__(self):
        return self.title

class Cats(models.Model):
    DISI= 1
    ERKEK = 2

    GENDER_CHOICES = (
        (1, 'Dişi'),
        (2, 'Erkek'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)
    title=models.CharField(verbose_name='Başlık',max_length=255)
    cat_type=models.ForeignKey(CatsType,on_delete=models.CASCADE)
    content = RichTextField(verbose_name='Hakkında')
    created_at=models.DateTimeField(auto_now_add=True)
    img = models.FileField(upload_to='img/')
    is_active=models.BooleanField(verbose_name='Aktif',default=False)
    is_mainpage = models.BooleanField(verbose_name='Ana Sayfa',default=False)

    def __str__(self):
        return self.title
