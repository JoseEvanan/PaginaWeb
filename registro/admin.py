from django.contrib import admin
from .models import Registro
from .models import Cita

# Register your models here.
admin.site.register(Cita)
admin.site.register(Registro)
