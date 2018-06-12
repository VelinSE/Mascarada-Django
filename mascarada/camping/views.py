from camping.models import Camping
from camping.forms import ReservationForm
from tickets.models import Visitor

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import random

@login_required
def reserve(request):
    campings = Camping.objects.all()

    if request.method == 'POST':
        form = ReservationForm(data=request.POST, email_options=Visitor.objects.filter(user = request.user))
        if form.is_valid():
            if form.save():
                return redirect('/tickets/my-tickets/') 
        return render(request, 'reserve.html', { 'form' : form , 'campings' : campings })
    else:
        form = ReservationForm(email_options=Visitor.objects.filter(user = request.user))
        args = { 'form' : form , 'campings' : campings}
        return render(request, 'reserve.html', args)

def seed_campings(request):
    for i in range(1, 49):
        camp = Camping.objects.get(id = i)
        camp.free_beds = random.randint(0,6)
        camp.save()

    return redirect('/camping/reserve/')

@login_required
def camping(request):
    campings = Camping.objects.all()
    camp_options = campings.values()
    bed_options = campings.order_by('free_beds').values('free_beds').distinct()
    
    if request.method == 'POST':
        form = ReservationForm(data=request.POST, email_options=Visitor.objects.filter(user = request.user), camp_options=camp_options, bed_options=bed_options)

        if form.is_valid():
            if form.save():
                return redirect('/tickets/my-tickets/')

        return render(request, 'camping.html', { 'form' : form , 'campings' : campings, })
    else:
        form = ReservationForm(email_options=Visitor.objects.filter(user = request.user), camp_options=camp_options, bed_options=bed_options)        
        args = { 'form' : form , 'campings' : campings, }

        return render(request, 'camping.html', args)

    
