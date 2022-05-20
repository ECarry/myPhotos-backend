from django.db import models


class Photo(models.Model):
    TYPE_CHOICES = [
        ('0', 'Person'),
        ('1', 'Nature')
    ]
    name = models.CharField(max_length=32, verbose_name="名称")
    time = models.DateField(verbose_name="拍摄时间")
    desc = models.TextField(verbose_name="简介")
    url = models.ImageField(upload_to='images/%Y/%m/%d/')
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, verbose_name="类型")
