from django.db.migrations import serializer
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from board.serializers import BoardSerializer
from rest_framework import generics, mixins, filters, viewsets, status

from board.models import Board


class BoardViewSet(viewsets.ViewSet):

    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    def list(self,request):
        queryset = Board.objects.all()
        serializer = BoardSerializer(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        queryset = Board.objects.all()
        board = get_object_or_404(queryset,pk=pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def update(self, request, pk=None):
        # update //
        board = self.get_object(pk)
        # 특정 인스턴스를 가져옵니다.
        serializer = BoardSerializer(board, data=request.data)
        # 업데이트 할 인스턴스가 올바른지 확인하기 위한 코드
        # 시리얼라이저 안에, 첫 번째로 인스턴스를 넣고, 두 번째에는 그 인스턴스에 들어갈
        # 외부에서 온 데이터를 넣습니다.
        if serializer.is_valid():
            # 바꿀 데이터가 올바르다면
            serializer.save()
            # 디비에 저장
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        board = self.get_object(pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'code', ]

class SearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
        return super(SearchFilter, self).get_search_fields(view, request)














# class BoardList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'code',]
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class BoardDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
