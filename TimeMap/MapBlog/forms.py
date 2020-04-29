from django import forms
from .models import UseDemand

class UseDemand(forms.ModelForm):
    class Meta:
        Model = UseDemand
        fields = ('name', 'place', 'num_people', 'purpose', 'start_time', 'finish_time')