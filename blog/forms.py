from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'duration', 'rental_start_date', 'rental_finish_date', 'sales_company',  )

