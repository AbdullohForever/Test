
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print("username: ", username, "password: ", password)
            user = authenticate(username=username, password=password)
            print("user: ", user)
            if user is not None:
                print("Logging")
                login(request, user)
                return redirect('question-list')  # Change this to the URL of the success page
            else:
                print("Not login")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
