from django.db import models
from core.models import CoreModel


class Board(CoreModel):

    title = models.CharField(max_length=140)
    sub_title = models.CharField(max_length=140)
    contents = models.CharField(max_length=1000, blank=True)
    view_cnt = models.IntegerField(default=1)
    user = models.name = models.ForeignKey('users.User', related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pk"]
