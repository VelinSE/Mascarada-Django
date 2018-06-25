from camping.models import Camping, Spot, Tent, Reservation
from tickets.models import Visitor
from tickets.utils import render_to_pdf

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import widgets
from django.core.mail import EmailMessage

import ast

TENT_OPTIONS = (
    ('0', 'None'),
    ('2', '2 Person, 15€'),
    ('4', '4 Person, 30€'),
    ('6', '6 Person, 45€'),
)

EMAIL_MESSAGE = """A camping reservation has been purchased for this email. You will be able to enter the camping site using your rfid. The camping number is %d and the reservation is for %d bed/s. """


class ReservationForm(forms.Form):

    def __init__(self, email_options=None, camp_options=None, bed_options=None, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['visitor_email'] = forms.MultipleChoiceField(
            widget=widgets.SelectMultiple, choices=ReservationForm.set_mail_choises(email_options), label='Visitors')
        self.fields['beds_taken'] = forms.ChoiceField(
            widget=widgets.Select, choices=ReservationForm.set_bed_choices(bed_options), label='Number of people')
        self.fields['camp_no'] = forms.ChoiceField(
            widget=widgets.Select, choices=ReservationForm.set_camp_choices(camp_options), label='Camping spot')
        self.fields['tent_size'] = forms.ChoiceField(
        widget=widgets.Select, choices=TENT_OPTIONS, label='Tent')

        self.fields['beds_taken'].widget.attrs = {'id': 'single'}
        self.fields['beds_taken'].widget.template_name = 'select_template.html'

        self.fields['camp_no'].widget.attrs = {'id': 'multiple'}
        self.fields['camp_no'].widget.template_name = 'multiselect_template.html'
        self.fields['camp_no'].widget.option_template_name = 'multiselect_option_template.html'

    def save(self, commit=True):
        isValid = True

        camp_entry_cleaned = ast.literal_eval(self.cleaned_data['camp_no'])
        camping = Camping.objects.get(camping_number=camp_entry_cleaned['camping_number'])
        spot = Spot(beds_taken=int(self.cleaned_data['beds_taken']))

        spot.camping = camping
        if camping.free_beds < spot.beds_taken:
            isValid = False
            self.add_error('beds_taken', "There are not %s free beds in this camping" % spot.beds_taken)
        else:
            camping.free_beds -= spot.beds_taken

        tent_size = self.cleaned_data['tent_size']
        tent = None
        if tent_size != '0':
           tent = Tent(size=int(tent_size))

        if isValid:
            if tent is not None:
                message_content = (EMAIL_MESSAGE % (camping.camping_number, spot.beds_taken)) + ("""The reservation includes a %s-person tent.""" % tent_size)
                tent.save()
            else:
                message_content = EMAIL_MESSAGE % (camping.camping_number, spot.beds_taken)
            camping.save()
            spot.save()
        
        for visitor in self.cleaned_data['visitor_email']:
            visitor_id, visitor_email = visitor.split()
            visitor_id = int(visitor_id)

            reservation = Reservation()
            reservation.spot = spot
            reservation.tent = tent
            reservation.visitor_id = int(visitor_id)
            reservation.save()
             
            msg = EmailMessage('Mascarada', message_content, to=[visitor_email])
            msg.send()

        return reservation


    def set_mail_choises(visitors):
        pairs = ()
        for v in visitors:
            single_pair = ((str(v.id) + " " + v.email, v.email),)
            pairs += single_pair
        return pairs

    def set_bed_choices(bed_options):
        l = list()

        for option in bed_options:
            if(option['free_beds'] != 0):
                l.append((option['free_beds'], option['free_beds']))
        return l

    def set_camp_choices(camp_options):
        l = list()

        for option in camp_options:
            if(option['id'] != 0 and option['free_beds'] != 0):
                l.append((option, option['id']))

        return l
