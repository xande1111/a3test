from django import forms
from .models import SocialNetwork

class SocialNetworkForm(forms.ModelForm):

    class Meta:
        model = SocialNetwork
        exclude = ()