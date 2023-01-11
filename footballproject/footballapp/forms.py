from django import forms
from .models import Football

class FootballForm(forms.ModelForm):
    class Meta:
        model=Football
        fields=['team_name','coach_name','desc','year','img']