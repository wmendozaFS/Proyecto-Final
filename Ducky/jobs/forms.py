from django import forms
from .models import JobOffer

class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        exclude = ['created_by', 'created_at', 'is_active']