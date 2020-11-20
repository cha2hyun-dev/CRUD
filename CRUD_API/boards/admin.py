from django.contrib import admin
from . import models


@admin.register(models.Board)
class BoardAdmin(admin.ModelAdmin):

    list_display = ("title", "sub_title", "view_cnt", "user")
