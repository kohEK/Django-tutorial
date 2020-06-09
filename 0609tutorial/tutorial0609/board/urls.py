from django.urls import path
from board import views

urlpatterns = [
    path('board/', views.BoardList.as_view()),
    path('board/<int:pk>/', views.BoardDetail.as_view()),
]
