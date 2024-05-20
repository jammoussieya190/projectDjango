
from .models import Transport
from .models import Event
from django import forms
from .models import Post
from .models import StageOffer
from .models import Logement


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'type']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'time', 'location', 'description']



class StageOfferForm(forms.ModelForm):
    class Meta:
        model = StageOffer
        fields = ['title', 'duration', 'location', 'description']
        
class LogementForm(forms.ModelForm):
    class Meta:
        model = Logement
        fields = ['nom', 'adresse', 'prix', 'description']
        from django import forms


class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['destination', 'departure_date', 'departure_time', 'vehicle', 'description']
        widgets = {
            'departure_date': forms.DateInput(attrs={'type': 'date'}),
            'departure_time': forms.TimeInput(attrs={'type': 'time'}),
        }

from django import forms
from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'content', 'image']
