from django.db import models
from accounts.models import CustomUser

class Diary(models.Model):
    #日記モデル:

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真１', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真２', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真３', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Dairy'

    def __str__(self):
        return self.title

