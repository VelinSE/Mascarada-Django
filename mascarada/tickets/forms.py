from datetime import datetime
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from tickets.models import Visitor


class VisitorCreationForm(ModelForm):
    class Meta:
        model = Visitor
        fields = (
            'first_name',
            'last_name',
            'email',
            'birth_date'
        )

        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'birth_date': widgets.DateInput(attrs={'class': 'datepicker'}),
        }

        

    def save(self, user, commit=True):
        visitor = super(VisitorCreationForm, self).save(commit=False)

        visitor.first_name = self.cleaned_data['first_name']
        visitor.last_name = self.cleaned_data['last_name']
        visitor.email = self.cleaned_data['email']
        visitor.birth_date = self.cleaned_data['birth_date']

        visitor.user = user
        visitor.event_money = 0
        visitor.rfid_code = None

        print(Visitor.objects.all().values('rfid_code'))

        if commit:
            visitor.save()

        return visitor
