from django.urls import path
from .views import BlogView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='delete'),
    path('post/<int:pk>/yoz' ,BlogUpdateView.as_view(),name='blog_edit'),
    path('post/new/',BlogCreateView.as_view(),name='post_new'),
    path('',BlogView.as_view(),name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='blog_detail'),
]