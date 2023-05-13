from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [

    path('', PostList.as_view()),
    path('news/', PostList.as_view()),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]

