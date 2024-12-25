from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class CreateNewPost(LoginRequiredMixin, CreateView):
    template_name = 'feed/create.html'
    model = Post
    fields = ['text']
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)