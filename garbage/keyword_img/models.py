from django.db import models

class Tag(models.Model):
    INITAIL = "00"
    INITED_NO_DOWNLAOD = "01"
    TAG_DOWN_LOAD_DETAIL_NO_COMPLETE = "02"
    NOT_CONNECTED = "03"
    OK = "100"
    DELETED = "999"
    STATUS_CHOICE=(
        (INITAIL, '默认值'),
        (INITED_NO_DOWNLAOD, '数据已录入,未下载'),
        (TAG_DOWN_LOAD_DETAIL_NO_COMPLETE, '详情未下载'),
        (NOT_CONNECTED, '未建立关联'),
        (OK, '数据可用'),
        (DELETED, '数据删除'),
    )
    name = CharField(max_length=200)
    related_tags = models.ManyToManyField("self");
    status = models.CharField(max_length=200, choices = STATUS_CHOICE, default=INITAIL)

class KeywordImg(models.Model):
    INITAIL = "00"
    INITED_NO_DOWNLAOD = "01"
    OK = "100"
    DELETED = "999"
    STATUS_CHOICE=(
        (INITAIL, '默认值'),
        (INITED_NO_DOWNLAOD, '数据已录入,未下载'),
        (OK, '数据可用'),
        (DELETED, '数据删除'),
    )
    keyword = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    url = models.CharField(max_length=300)
    filepath = models.CharField(max_length=300)
    status = models.CharField(max_length=200, choices = STATUS_CHOICE, default="00")

class TagImg(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    img = models.ForeignKey(KeywordImg, on_delete=models.CASCADE)
