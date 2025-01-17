from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "user/register.html"
    success_url = reverse_lazy("login")
