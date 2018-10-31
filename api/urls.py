from django.urls import path, include
from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import ComplaintViewSet, api_root


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'complaints', ComplaintViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
