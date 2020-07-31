from django import forms
from django.forms import ModelForm
from crud.models import Instrumento

class InstrumentoCreationForm(forms.ModelForm):
    class Meta:
        model = Instrumento                         #Tipo de obj que o forms vai criar
        fields = ['loja', 'tipo', 'marca', 'foto']  #Campos que o forms vai ter (mesmos do model)
        widgets = {                                 #Características específicas de alguns campos
            'loja': forms.HiddenInput(),            #Esconder no frontend o campo loja
        }