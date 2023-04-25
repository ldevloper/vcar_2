from django.contrib import admin
from .models import Cliente, Aluguel, Carro

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Aluguel)

