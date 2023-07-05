from rest_framework import serializers
from .models import IconLink


class IconLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconLink
        fields = '__all__'
