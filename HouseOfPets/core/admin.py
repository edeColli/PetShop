from django.contrib import admin
from .models import Reserva
# Register your models here.

#class ReservaAdmin(admin.ModelAdmin):
#    readonly_fields = ("dreated")

admin.site.register(Reserva)
