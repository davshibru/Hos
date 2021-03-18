from django.contrib import admin
from .models import Doctors, Reception, TimesOfWork

admin.site.register(Doctors)
admin.site.register(Reception)
admin.site.register(TimesOfWork)
