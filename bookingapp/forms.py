from django import forms
from .models import Movie, MovieBooking

class MovieBookingForm(forms.ModelForm):
    class Meta:
        model = MovieBooking
        fields = '__all__'