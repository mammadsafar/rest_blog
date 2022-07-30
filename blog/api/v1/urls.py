from django.urls import path, include
from blog.api.v1 import views

app_name = 'api-v1'

urlpatterns = [
    path('post/', views.api_post_list_view, name='api_post_list_view'),

]
