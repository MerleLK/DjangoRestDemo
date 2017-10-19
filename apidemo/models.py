from django.db import models


class Comment(models.Model):
    email = models.EmailField(

    )
    additional_param = models.CharField(
        verbose_name="额外参数",
        max_length=20,
        default="simple",
    )
    content = models.CharField(
        max_length=200,
        verbose_name="内容"
    )
    created = models.DateTimeField(
        verbose_name="创建时间",
        auto_now=True,
    )


class Event(models.Model):
    description = models.CharField(
        verbose_name="描述",
        max_length=200,
    )
    start = models.DateTimeField()
    finish = models.DateTimeField()

    name = models.CharField(
        verbose_name="名字",
        max_length=30,
    )
    room_number = models.IntegerField()
    date = models.DateField()


class GameRecord(models.Model):
    score = models.IntegerField()


class Account(models.Model):
    pur_amount = models.IntegerField()
