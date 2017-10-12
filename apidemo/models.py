from django.db import models


class Comment(models.Model):
    email = models.EmailField(

    )
    content = models.CharField(
        max_length=200,
        verbose_name="内容"
    )
    created = models.DateTimeField(
        verbose_name="创建时间",
        auto_now=True,
    )
