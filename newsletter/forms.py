from django import forms
from .models import Subscriber


class SubscribeForm(forms.ModelForm):
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(
            attrs={'class': 'border-0 border-bottom', 'placeholder': 'Email for Subscription'})
    )

    class Meta:
        model = Subscriber
        fields = '__all__'
        

# widget = forms.EmailInput(
#     attrs={'class': 'form-control w-75 border-0 border-bottom', 'placeholder': 'Email for Subscription'})
