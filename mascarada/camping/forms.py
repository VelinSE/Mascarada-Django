from camping.models import Camping, Spot, Tent, Reservation
from tickets.models import Visitor

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class ReservationForm(forms.Form):
    camp_no = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(48)])
    visitor_email = forms.EmailField()
    beds_taken = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])


    def save(self, tent_size, commit = True):
        camping = Camping.objects.filter(camping_number = self.cleaned_data['camp_no']).first()
        visitor = Visitor.objects.filter(email = self.cleaned_data['visitor_email']).first()

        spot = Spot(beds_taken = self.cleaned_data['beds_taken']) 
        spot.camping = camping

        camping.free_beds -= spot.beds_taken

        camping.save()
        spot.save()

        tent = None
        if tent_size != '0':
            tent = Tent(size=int(tent_size))
            tent.save()

        reservation = Reservation()
        reservation.spot = spot
        reservation.tent = tent
        reservation.visitor = visitor

        reservation.save()

        return reservation
