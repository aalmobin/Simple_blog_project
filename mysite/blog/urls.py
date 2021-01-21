from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post_lists/<str:username>/', UserPostListView.as_view(), name='post-lists'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post_create/NEW/', PostCreateView.as_view(), name='post-create'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
]
