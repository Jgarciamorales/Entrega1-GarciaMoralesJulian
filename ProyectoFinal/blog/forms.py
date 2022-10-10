from django import forms


class formAutor(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    profesion = forms.CharField()


class formArticulo(forms.Form):

    titulo = forms.CharField()
    texto = forms.CharField()


class formSeccion(forms.Form):

    nombre = forms.CharField()
