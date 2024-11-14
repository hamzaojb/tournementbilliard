from django import forms
from .models import Registration
from .models import Publication  # Assurez-vous que le modèle Publication est correctement importé


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'image']
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'content', 'image']