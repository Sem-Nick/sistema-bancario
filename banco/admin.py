from django.contrib import admin

from .models import Cliente, Cartao, Emprestimo

admin.site.register(Cliente)
admin.site.register(Cartao)
admin.site.register(Emprestimo)
# Register your models here.
