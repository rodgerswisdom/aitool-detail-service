from django.contrib import admin
from .models import Tool
from import_export.admin import ImportExportModelAdmin
from .resource import ToolResource
from django import forms


class ToolAdmin(ImportExportModelAdmin):
  tool_class = ToolResource

admin.site.register(Tool, ToolAdmin)