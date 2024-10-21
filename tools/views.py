import requests
from django.shortcuts import render
from rest_framework import viewsets
from .models import Tool
from .serializers import ToolSerializer
from django.conf import settings
from django.http import JsonResponse

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

    def retrieve(self, request, *args, **kwargs):
        tool = self.get_object()
        category_api_url = f'{settings.CATEGORY_SERVICE_URL}/api/categories/{tool.category_id}/'
        category_response = requests.get(category_api_url)

        if category_response.status_code == 200:
            category_data = category_response.json()
            tool_data = {
                'id': tool.id,
                'name': tool.name,
                'description': tool.description,
                'website_link': tool.website_link,
                'youtube_link': tool.youtube_link,
                'category': category_data  # Category info from category-service
            }
            return JsonResponse(tool_data)
        return JsonResponse({'error': 'Category not found'}, status=404)
