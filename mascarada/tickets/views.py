from tickets.models import Visitor, EntryTicket
from tickets.forms import VisitorCreationForm
from custom_auth.models import CustomUser
from tickets.utils import render_to_pdf

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.core.mail import EmailMessage

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
            return redirect('/tickets/success')   
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

@login_required
def success(request):
    return render(request, 'success_tickets.html')

@csrf_exempt
def resend_qr(request):
    visitor = Visitor.objects.get(id=int(request.POST.get('visitorId')))
    ticket = EntryTicket.objects.get(visitor_id=visitor.id)
    
    args = { 'text' : ticket.qr_code, 'visitor' : visitor }
    pdf = render_to_pdf('purchase_email.html', args)
    response = HttpResponse(pdf, content_type='application/pdf')

    msg = EmailMessage('Mascarada', 'Welcome to mascarada!', to=[visitor.email])
    msg.attach('ticket.pdf', response.content , 'application/pdf')
    msg.send()
    return JsonResponse({ 'success' : True })
