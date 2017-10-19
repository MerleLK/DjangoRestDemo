from django.db import models
from django.contrib.auth.decorators import login_required


class Account(models.Model):

    username = models.CharField(
        max_length=30,
        verbose_name="用户名",
    )
    password = models.CharField(
        max_length=30,
        verbose_name="密码",
    )


class TimeStampedModel(models.Model):
    """
    Simple abstract base class.
    provide the general created time, update time fields.
    可以将 公用的字段抽取出来。
    """
    created_at = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="更新时间",
        auto_now=True,
    )

    class Meta:
        abstract = True


class Article(TimeStampedModel):
    title = models.CharField(
        max_length=200,
    )
