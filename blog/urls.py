from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update',),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete',),

]
