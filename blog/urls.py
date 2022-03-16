from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('postlist/', views.PostListView.as_view(), name='post_list'),
    # path('postlist/', views.postlist, name='post_list'),
    path('postditail/<int:year>/<int:month>/<int:day>/<slug:post>/', views.postdetail, name='post_detail'),
]
