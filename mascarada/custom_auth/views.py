from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from custom_auth.models import CustomUser
from custom_auth.forms import RegistrationForm

from tickets.models import Visitor
from camping.models import Reservation, Spot, Tent


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.pk is not None:
                return redirect('/accounts/profile/')
        return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'register.html', args)


@login_required
def profile(request):
    user = request.user
    tickets = Visitor.objects.filter(user=request.user)
    campings = list()

    for visitor in tickets:
        reservations = Reservation.objects.filter(visitor=visitor)

        for reservation in reservations:
            res_visitor = reservation.visitor
            tent = None
            camp_spot = Spot.objects.get(id=reservation.spot_id)
            if reservation.tent_id is not None:
                tent = Tent.objects.get(id=reservation.tent_id)
                
            campings.append({'spot' : camp_spot, 'tent' : None, 'visitor': res_visitor})

    args = {'user': user, 'tickets': tickets, 'campings' : campings}

    return render(request, 'profile.html', args)


def logout_user(request):
    logout(request)
    args = {}
    return redirect(reverse('index'))
