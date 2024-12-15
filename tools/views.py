from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

import requests
from django.shortcuts import render
from rest_framework import viewsets
from .models import Tool
from .serializers import ToolSerializer
from django.conf import settings
from django.http import JsonResponse
# from rest_framework.pagination import LimitOffsetPagination

# class ToolPagination(LimitOffsetPagination):
   # default_limit = 50  # Default items per page
   # max_limit = 100

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    # pagination_class = ToolPagination

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
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
