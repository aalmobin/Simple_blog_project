from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegisterForm, UpdateUser
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class Register(View):
    """The Register page View"""

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account Has Been Created For {user}')
            return redirect('login')


class Profile(LoginRequiredMixin, View):
    """The profile page view"""

    def get(self, request, *args, **kwargs):
        return render(request, 'users/profile.html')


class ProfileUpdate(View):
    """The Update profile page view"""

    def get(self, request, *args, **kwargs):
        u_form = UpdateUser(instance=request.user)
        context = {
            'u_form': u_form,
        }
        return render(request, 'users/update_profile.html', context)

    def post(self, request, *args, **kwargs):
        u_form = UpdateUser(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('profile')