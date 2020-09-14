from django.contrib import admin
from User.models import *
# Register your models here.


class usuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email')
    search_fields = ('nombre', 'email')


class notaAdmin(admin.ModelAdmin):
#    list_display = ('id_usuario_id', 'titulo', 'fecha')
    list_filter = ('fecha', 'check',)
    date_hierarchy = 'fecha'


admin.site.register(usuario, usuarioAdmin)
admin.site.register(nota, notaAdmin)