from django.urls import path
from . import views as accounts_views
from django.contrib.auth import views

from .forms import UserLoginForm
urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    ),
    path('signup/', accounts_views.SignUpView.as_view(), name='signup'),

]
