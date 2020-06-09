from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from board import views
from board.views import BoardViewSet

router = SimpleRouter()
router.register(r'board', BoardViewSet, basename='Board')


urlpatterns = [
#     # path('board/', views.BoardList.as_view()),
#     # path('board/<int:pk>/', views.BoardDetail.as_view()),
]
urlpatterns += router.urls
#
# urlpatterns = format_suffix_patterns(urlpatterns)
