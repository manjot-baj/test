from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportModelAdmin
@admin.register(Details)
class View_admin(ImportExportModelAdmin):
    pass