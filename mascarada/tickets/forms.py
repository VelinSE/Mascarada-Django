from datetime import datetime
from django.forms import ModelForm
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

    def save(self, user, commit = True):
        visitor = super(VisitorCreationForm, self).save(commit=False)

        visitor.first_name = self.cleaned_data['first_name']
        visitor.last_name = self.cleaned_data['last_name']
        visitor.email = self.cleaned_data['email']
        visitor.birth_date = self.cleaned_data['birth_date']

        visitor.user = user
        visitor.event_money = 0

        if commit:
            visitor.save()
        
        return visitor
