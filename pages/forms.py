from django import forms
from pages.models import ResevationModel

class ReservationForm(forms.ModelForm):
    class Meta:
        model = ResevationModel
        fields = ['name', 'phone_number', 'email', 'num_people', 'date']