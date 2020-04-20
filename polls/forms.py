from django.db import models
from django import forms
from .models import UserInformation, UserHappinessData

class HappinessForm(forms.Form):
    sleep = forms.IntegerField(label='Sleep', max_value=24, min_value=0, widget=forms.NumberInput(
        attrs={
            "id":"sleep"
        }
    ))

    exercise = forms.IntegerField(label='Exercise', max_value=24, min_value=0, widget=forms.NumberInput(
        attrs={
            "id":"exercise"
        }
    ))

    social = forms.IntegerField(label='Social', max_value=24, min_value=0, widget=forms.NumberInput(
        attrs={
            "id":"social"
        }
    ))

    metime = forms.IntegerField(label='Metime', max_value=24, min_value=0, widget=forms.NumberInput(
        attrs={
            "id":"metime"
        }
    ))

    weather = forms.IntegerField(label='Weather',max_value=10, min_value=0,  widget=forms.NumberInput(
        attrs={
            "id":"weather",
            "placeholder": "rating from 1-10"

        }
    ))

    socialmedia = forms.IntegerField(label='Social Media',max_value=24, min_value=0,  widget=forms.NumberInput(
        attrs={
            "id":"socialmedia"

        }
    ))

    happy = forms.IntegerField(label='Happiness', max_value=10, min_value=0, widget=forms.NumberInput(
        attrs={
            "id":"happy",
            "placeholder": "rating from 1-10"

        }
    ))

    

    
        
