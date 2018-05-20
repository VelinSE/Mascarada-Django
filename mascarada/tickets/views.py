from django.shortcuts import render, redirect
from tickets.forms import VisitorCreationForm
from tickets.models import Visitor
from django.core.mail import EmailMessage
from tickets.utils import render_to_pdf
from django.http import HttpResponse

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

def my_tickets(request):
    tickets = Visitor.objects.filter(user = request.user)
    args = { 'tickets' : tickets }
    return render(request, 'my-tickets.html', args)

def sad(request):
    args = { 'text' : '1q2w3e4r5t' }
    html_content = render(request, 'purchase_email.html', args)
    msg = EmailMessage('Mascarada', html_content, 'team@mascarada.com', [request.user.email])
    msg.content_subtype = "html"
    msg.send()
    return render(request, 'purchase_email.html', args)

def sadd(request):
    args = { 'text' : '1q2w3e4r5t' }
    pdf = render_to_pdf('purchase_email.html', args)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Invoice_%s.pdf" %("12341231")
    content = "attachment; filename='%s'" %(filename)
    response['Content-Disposition'] = content


    msg = EmailMessage('Mascarada', 'Welcome to mascarada!', 'team@mascarada.com', [request.user.email])
    msg.attach('ticket.pdf', content, 'application/pdf')
    msg.send()
    return render(request, 'purchase_email.html', args)
