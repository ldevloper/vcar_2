from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import forms
from .models import Cliente, Aluguel, Carro

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Aluguel)


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User 
        fields = forms.UserCreationForm.Meta.fields + ('email','first_name','last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

