from django import forms
from django.contrib.auth.models import User



class ChatGptForm(forms.Form):

    meals = (("1", "Breakfast"), ("2", "Lunch"), ("3", "Dinner"))

    meal_choice = forms.ChoiceField(choices=meals)