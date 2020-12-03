from django.db import models

# Create your models here.


class Topics(models.Model):
    Categroy_type = (
        (0, u'技术类'),
        (1, u'非技术类')
    )

    title = models.CharField(max_length=30, verbose_name='文章标题')
    categroy = models.CharField(max_length=10, choices= Categroy_type, default=0, verbose_name='文章分类')
    content = models.TextField(verbose_name='文章内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        db_table = 'Topics'
        verbose_name = u'文章信息'
        verbose_name_plural = '文章信息'

