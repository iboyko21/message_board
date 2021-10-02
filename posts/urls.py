from django.urls import path
from .views import (
     PostListView, 
     PostUpdateView, 
     PostDetailView, 
     PostDeleteView,
     PostCreateView,
     AddCommentView,
     LikeView
 )


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment_to_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
]