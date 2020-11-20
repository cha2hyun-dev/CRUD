from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from .models import Board
from .serializers import BoardSerializer

# Create your views here.


class BoardsViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
