from import_export import resources
from .models import Tool  

class ToolResource(resources.ModelResource):
  class Meta:
    model = Tool
