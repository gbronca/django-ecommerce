from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form': form})

