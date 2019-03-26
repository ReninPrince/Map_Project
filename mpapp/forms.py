from django import forms
# from django.core import validators
from mpapp.models import maps
from mpapp.choices import *


class NFormName(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = maps
        fields = '__all__'


class DFormName(forms.Form):
    holiday = forms.ChoiceField(choices = holiday_CHOICES, label="Where do you want to go for your dream holiday:", initial='2', widget=forms.Select(), required=True)
    languages = forms.ChoiceField(choices = languages_CHOICES, label="What are the languages you can speak:", initial='1', widget=forms.Select(), required=True)
    nathis = forms.ChoiceField(choices = nathis_CHOICES, label="Do you like natural or historical plces?", initial='1', widget=forms.Select(), required=True)
    time = forms.ChoiceField(choices = time_CHOICES, label="How much time do you like spending outdoors?", initial='1', widget=forms.Select(), required=True)
    soqu = forms.ChoiceField(choices = soqu_CHOICES, label="Do you like sounded place or quiet place?", initial='1', widget=forms.Select(), required=True)
    Relationship = forms.ChoiceField(choices = Relationship_CHOICES, label="Status of your Relationship", initial='1', widget=forms.Select(), required=True)
    preference = forms.ChoiceField(choices = preference_CHOICES, label="What is your preference?", initial='1', widget=forms.Select(), required=True)
    foodie = forms.ChoiceField(choices = foodie_CHOICES, label="What kind of foodie are you?", initial='1', widget=forms.Select(), required=True)
    stress = forms.ChoiceField(choices = stress_CHOICES, label="What is your stress buster?", initial='1', widget=forms.Select(), required=True)

class MFormName(forms.Form):
    search = forms.CharField(max_length=100,
                           widget= forms.TextInput(attrs={'id':'pac-input'}))
