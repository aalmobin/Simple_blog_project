from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegisterForm
from django.contrib import messages


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

