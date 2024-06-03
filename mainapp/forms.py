from django import forms

class EventForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    date = forms.DateInput()
    place = forms.CharField(max_length=100)
    

class LugarEventoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del Lugar")
    direccion = forms.CharField(widget=forms.Textarea, label="Dirección")
    ciudad = forms.CharField(max_length=100, label="Ciudad")
