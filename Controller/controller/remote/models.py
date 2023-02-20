from django.db import models
from enum import unique
# Create your models here.

class Remote(models.Model):
    id  = models.BigAutoField("auto", primary_key=True)
    type = models.IntegerField()
    ip = models.CharField('서버 아이피',max_length = 20,unique=True)
    name = models.CharField('서버 이름',max_length=20)
    rootpw = models.CharField('서버 비번',max_length=20)
    cloud = models.CharField('상위 서버 아이피',max_length=20)

class ModuleField(models.Model):
    remote_id = models.ForeignKey(Remote,related_name= 'remote',on_delete=models.CASCADE, default=Remote.objects.first())
    priority = models.IntegerField('우선순위')
    name = models.CharField('모듈 이름', max_length=20)
    giturl = models.CharField('모듈 깃헙', max_length = 50)
    install = models.TextField('설치 스크립트')
    execute = models.TextField('실행 스크립트')
    envs = models.JSONField('환경변수')
    