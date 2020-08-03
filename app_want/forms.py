from django import forms
from .models import texto, usuario
from django.contrib.auth.forms import User

class CadastrarForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nome']
    senha=forms.CharField(widget=forms.PasswordInput)

class escreverForm(forms.ModelForm):
    class Meta:
        model = texto
        fields = ['titulo','corpo']


