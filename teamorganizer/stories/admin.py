from functools import partial, update_wrapper
from gettext import ngettext

from django.contrib import admin, messages
from django.utils.translation import gettext as _

# Register your models here.
from django.contrib.admin import helpers
from django.contrib.admin.options import csrf_protect_m, IncorrectLookupParameters
from django.contrib.admin.utils import model_ngettext
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.urls import path

from .models import Storie, Step

def kanban_view(request):
    return HttpResponse('Admin Custom View')







admin.site.register(Storie)
admin.site.register(Step)
