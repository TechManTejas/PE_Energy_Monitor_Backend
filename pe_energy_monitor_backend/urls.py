from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from icon_link.views import IconLinkViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'icon-links', IconLinkViewSet, basename='icon-links')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
