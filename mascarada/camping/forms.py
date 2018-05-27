from camping.models import Camping, Spot, Tent, Reservation
from tickets.models import Visitor

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

TENT_OPTIONS = (
    ('0', 'None'),
    ('2', '2 Person'),
    ('4', '4 Person'),
    ('6', '6 Person'),
)

EMAIL_OPTIONS = ()

class ReservationForm(forms.Form):

    def __init__(self, email_options = None, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['visitor_email'] = forms.ChoiceField(widget=forms.RadioSelect(), choices=ReservationForm.set_mail_choises(email_options)) 
    

    camp_no = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(48)])
    beds_taken = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    tent_size = forms.ChoiceField(widget=forms.RadioSelect, choices=TENT_OPTIONS)

    def save(self, commit = True):
        isValid = True
        camping = Camping.objects.filter(camping_number = self.cleaned_data['camp_no']).first()
        visitor_id = self.cleaned_data['visitor_email']
        spot = Spot(beds_taken = self.cleaned_data['beds_taken']) 
        spot.camping = camping


        if camping.free_beds < spot.beds_taken:
            print('invalid')
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
                tent.save()
            camping.save()
            spot.save()
            
            reservation = Reservation()
            reservation.spot = spot
            reservation.tent = tent
            reservation.visitor_id = int(visitor_id)

            reservation.save()
            return reservation
        

    def set_mail_choises(visitors):
        pair = ()
        for v in visitors:
            single_pair = ((str(v.id), v.email),)
            pair += single_pair
        return pair









    
