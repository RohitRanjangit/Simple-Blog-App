from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
    path('blog-home/',PostListView.as_view(),name = 'blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),
    path('post-create/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<str:username>/',UserPostListView.as_view(),name = 'user-post'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name = 'post-delete'),
    path('blog-about/',views.about,name = 'blog-about'),
]

