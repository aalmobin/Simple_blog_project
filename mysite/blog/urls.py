from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post_create/NEW/', PostCreateView.as_view(), name='post-create'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
]
