from .models import *
from django import forms


class ParsingForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        label="City",
        required=True,
        )
    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        label="District",
        required=False,
        empty_label='Все районы',
        initial='Все районы'
        )
    metro = forms.ModelChoiceField(
        queryset=Metro.objects.all(),
        label="Metro",
        required=False,
        empty_label='Все станции метро',
        initial='Все станции метро'
        )
    numrooms = forms.ModelChoiceField(
        queryset=Rooms.objects.all(),
        label="Number of rooms",
        required=False,
        empty_label='Любое количество'
        )

