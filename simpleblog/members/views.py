from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class UserLoginView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'members/login.html'

class UserEditView(generic.UpdateView):
    form_class = EditForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user