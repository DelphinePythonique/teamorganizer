from django.contrib import admin

# Register your models here.
from django.urls import path

from .models import Storie, Step


admin.site.register(Storie)
admin.site.register(Step)
