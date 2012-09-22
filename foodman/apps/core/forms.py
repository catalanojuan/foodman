
from django import forms
from django.contrib.auth.models import User

def get_choices():
    count = User.objects.filter(is_active=True).count()

    return tuple([(a,a) for a in range(1,count+1)])

class ChooseForm(forms.Form):
    num_choices = forms.ChoiceField(choices=get_choices(), widget=forms.widgets.Select(attrs={'class': 'span1'}))
