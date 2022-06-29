from django.shortcuts import render, reverse, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# from .models import Post
# from .forms import PostForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
