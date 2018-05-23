from camping.models import Camping
from camping.forms import ReservationForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import random

@login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        tent = request.POST.get('tent')
        if form.is_valid():
            form.save(tent)
            return redirect('/tickets/my-tickets/') 
        return render(request, 'reserve.html', { 'form' : form })
    else:
        form = ReservationForm()
        args = { 'form' : form }
        return render(request, 'reserve.html', args)

def seed_campings(request):
    for i in range(1, 49):
        camp = Camping.objects.get(id = i)
        camp.free_beds = random.randint(0,6)
        camp.save()

    return redirect('/camping/reserve/')