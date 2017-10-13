from django.db import models


class Account(models.Model):

    username = models.CharField(
        max_length=30,
        verbose_name="用户名",
    )
    password = models.CharField(
        max_length=30,
        verbose_name="密码",
    )
