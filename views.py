from django.shortcuts import render, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from accounts.services.forms import MyUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
# Create your views here.
User = get_user_model()

class DefaultLoginView(LoginView):

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('accounts:profile', kwargs={
         'pk': self.request.user.pk, #'username': self.request.user.username,
        })


class Register(CreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = 'registration/register.html'



class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'
