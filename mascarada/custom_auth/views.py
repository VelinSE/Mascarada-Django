from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required

from custom_auth.models import CustomUser
from custom_auth.forms import RegistrationForm

@login_required
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.pk is not None:
                return redirect('/accounts/profile/')
        return render(request, 'register.html', {'form' : form })
    else:
        form = RegistrationForm()
        args = {'form' : form }
        return render(request, 'register.html', args)

@login_required
def profile(request):
    user = request.user
    args = { 'user' : user}
    return render(request, 'profile.html', args)

def logout_user(request):
    logout(request)
    args = {}
    return render(request, 'logout_success.html', args)
