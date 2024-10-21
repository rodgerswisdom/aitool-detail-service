from rest_framework import serializers
from .models import Tool

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['id', 'name', 'description', 'website_link', 'youtube_link', 'category_id']
        # fields = ['id', 'name', 'description', 'website_link', 'youtube_link']
