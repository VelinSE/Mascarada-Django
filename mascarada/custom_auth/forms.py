from datetime import datetime
from django.contrib.auth.forms import UserCreationForm

from custom_auth.models import CustomUser

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.last_login = datetime.now()
        user.date_joined = datetime.now()

        if commit:
            user.save()
        
        return user
