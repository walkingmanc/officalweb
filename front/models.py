# Create your models here.

from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):  # 在python2版本中使用的是__unique__
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class CaseCat(models.Model):
    """案例分类"""
    name = models.CharField(max_length=20)
    order = models.PositiveIntegerField()


class CaseShow(models.Model):
    """首页案例展示"""
    picUrl = models.FilePathField(path='/home/images')
    iconUrl = models.FilePathField(path='/home/images')
    tips = models.CharField(max_length=200)
    intro = models.CharField(max_length=500)
    caseLogo = models.FilePathField(path='/home/images')
    visitUrl = models.URLField()
    previewPic = models.FilePathField(path='/home/images')
    caseCat = models.ForeignKey(CaseCat, on_delete=models.CASCADE)


class CaseShowDetailMulti(models.Model):
    """案例详情页中的多张图片展示"""
    detailPicUrl = models.FilePathField(path='/home/images')
    detailPicTips = models.CharField(max_length=50)
    order = models.PositiveIntegerField()
    caseShow = models.ForeignKey(CaseShow, on_delete=models.CASCADE)


class ServiceShow(models.Model):
    """首页服务项目展示"""
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    normalPic = models.FilePathField(path='/home/images')
    hiLightPic = models.FilePathField(path='/home/images')


class ProductShow(models.Model):
    """产品项目展示"""
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    listPic = models.FilePathField(path='/home/images')
    keyWords = models.CharField(max_length=50)


class GuestCollect(models.Model):
    """客户需求收集"""
    guestName = models.CharField(max_length=10)
    guestTel = models.CharField(max_length=20)
    guestRequire = models.FilePathField(max_length=100)

