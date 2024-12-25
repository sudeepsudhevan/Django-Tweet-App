from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Post


class HomePage(ListView):
    http_method_names = ['get']     # only allow GET requests
    template_name = 'feed/homepage.html'
    model = Post
    context_object_name = 'posts'   # default is object
    queryset = Post.objects.all().order_by('-id')[:30]


class PostDetailView(DetailView):
    http_method_names = ['get']     # only allow GET requests
    template_name = 'feed/detail.html'
    model = Post
    context_object_name = 'post'


class CreateNewPost(CreateView):
    template_name = 'feed/create.html'
    model = Post
    fields = ['text']
    success_url = '/'