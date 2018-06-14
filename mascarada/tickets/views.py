from tickets.models import Visitor
from tickets.forms import VisitorCreationForm
from custom_auth.models import CustomUser

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def buy_tickets(request):
    if  request.method == 'POST':
        form = VisitorCreationForm(request.POST)
        if form.is_valid():
            visitor = form.save(request.user)
            return redirect('/tickets/my-tickets/')   
        else:
            args = {'form' : form }
            return render(request, 'buy-tickets.html', args)                 
    else:
        form = VisitorCreationForm()
        args = {'form' : form }
        return render(request, 'buy-tickets.html', args)

@login_required
def my_tickets(request):
    tickets = Visitor.objects.filter(user = request.user)
    args = { 'tickets' : tickets }
    return render(request, 'my-tickets.html', args)

@login_required
def tickets(request):
    if  request.method == 'POST':
        form = VisitorCreationForm(request.POST)
        if form.is_valid():
            visitor = form.save(request.user)
            return redirect('/accounts/profile/#tickets')   
        else:
            args = {'form' : form }
            return render(request, 'tickets.html', args)                 
    else:
        visitor = CustomUser.objects.get(email=request.user)
        initial = {
                'first_name': visitor.first_name,
                'last_name': visitor.last_name,
                'email': visitor.email,    
            }
        form = VisitorCreationForm(initial=initial)
        args = {'form' : form }
        return render(request, 'tickets.html', args)


