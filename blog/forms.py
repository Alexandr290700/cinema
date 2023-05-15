from django import forms
from .models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[MinValueValidator(50), MaxValueValidator(500)]
    )


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
            "name",
            "duration",
            "rental_start_date",
            "rental_finish_date",
            "sales_company",
        )
