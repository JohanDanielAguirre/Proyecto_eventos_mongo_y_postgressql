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

class EventLocationForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre del Lugar")
    direccion = forms.CharField(widget=forms.Textarea, label="Dirección")
    ciudad = forms.CharField(max_length=100, label="Ciudad")

class UserForm(forms.Form):
    id = forms.CharField(max_length=100)
    nombreUsuario = forms.CharField(max_length=100, label='Nombre de Usuario')
    nombreCompleto = forms.CharField(max_length=100, label='Nombre Completo')
    tipoRelacion = forms.CharField(label='Tipo de realción', widget=forms.Select(
        choices=[('profesor', 'Profesor'), ('estudiante', 'Estudiante'), ('graduado', 'Graduado')
                 , ('empresario', 'Empresario'), ('administrativo', 'Administrativo'), ('directivo', 'Directivo')]))
    email = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)