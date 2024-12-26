from django.contrib.auth.models import User
from django.views.generic import DetailView

from .models import Profile


class ProfileDetailView(DetailView):
    http_method_names = ['get']     # only allow GET requests
    model = User
    template_name = 'profiles/detail.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
