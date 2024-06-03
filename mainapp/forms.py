from django import forms

class EventForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    date = forms.DateInput()
    place = forms.CharField(max_length=100)