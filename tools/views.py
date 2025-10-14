from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

import requests
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tool
from .serializers import ToolSerializer
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status

from .authentication import SimpleTokenAuthentication
# from rest_framework.pagination import LimitOffsetPagination

# class ToolPagination(LimitOffsetPagination):
   # default_limit = 50  # Default items per page
   # max_limit = 100

class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    authentication_classes = [SimpleTokenAuthentication]
    # pagination_class = ToolPagination

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    @method_decorator(vary_on_headers('Authorization'))
    def retrieve(self, request, *args, **kwargs):
        tool = self.get_object()
        category_api_url = f'{settings.CATEGORY_SERVICE_URL}/api/categories/{tool.category_id}/'
        headers = {}
        gate_token = getattr(settings, 'GATEKEEPER_TOKEN', None)
        if gate_token:
            headers['Authorization'] = f'Bearer {gate_token}'

        category_response = requests.get(category_api_url, headers=headers)

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


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {'detail': 'Email and password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        expected_email = getattr(settings, 'GATEKEEPER_EMAIL', None)
        expected_password = getattr(settings, 'GATEKEEPER_PASSWORD', None)
        access_token = getattr(settings, 'GATEKEEPER_TOKEN', None)

        if not expected_email or not expected_password or not access_token:
            return Response(
                {'detail': 'Authentication service is not configured.'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        if email != expected_email or password != expected_password:
            return Response(
                {'detail': 'Invalid email or password.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response({'access_token': access_token, 'email': expected_email})
