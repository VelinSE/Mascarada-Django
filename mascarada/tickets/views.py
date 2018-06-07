from tickets.models import Visitor
from tickets.forms import VisitorCreationForm

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

def tickets(request):
    if  request.method == 'POST':
        form = VisitorCreationForm(request.POST)
        if form.is_valid():
            visitor = form.save(request.user)
            return redirect('/tickets/my-tickets/')   
        else:
            args = {'form' : form }
            return render(request, 'tickets.html', args)                 
    else:
        form = VisitorCreationForm()
        args = {'form' : form }
        return render(request, 'tickets.html', args)


