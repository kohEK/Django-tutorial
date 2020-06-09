from django.shortcuts import render
from board.serializers import BoardSerializer
# Create your views here.
from rest_framework import generics

from board.models import Board


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer