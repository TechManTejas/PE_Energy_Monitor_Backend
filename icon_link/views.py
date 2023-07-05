from rest_framework import viewsets
from .models import IconLink
from .serializers import IconLinkSerializer


class IconLinkViewSet(viewsets.ModelViewSet):
    queryset = IconLink.objects.all()
    serializer_class = IconLinkSerializer
