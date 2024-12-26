from django.contrib.auth.models import User
from django.views.generic import DetailView

from feed.models import Post
from .models import Profile


class ProfileDetailView(DetailView):
    http_method_names = ['get']     # only allow GET requests
    model = User
    template_name = 'profiles/detail.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author=user).count()  # get the total number of posts
        return context
