from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        exclude = ("")
        read_only_fields = ("title", "sub_title", "view_cnt", "user", "contents")
