from django import forms

class EventForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    categoria = forms.CharField(max_length=100)
    fecha = forms.DateInput()
    lugar = forms.CharField(max_length=100)

    widgets = {
        fecha: forms.DateInput(attrs={'class': 'form-control datepicker'}),
    }

class UserForm(forms.Form):
    id = forms.CharField(max_length=100)
    nombreUsuario = forms.CharField(max_length=100)
    nombreCompleto = forms.CharField(max_length=100)
    tipoRelacion = forms.CharField(label='Tipo de realción', widget=forms.Select(
        choices=[('profesor', 'Profesor'), ('estudiante', 'Estudiante'), ('graduado', 'Graduado')
                 , ('empresario', 'Empresario'), ('administrativo', 'Administrativo'), ('directivo', 'Directivo')]))
    email = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)