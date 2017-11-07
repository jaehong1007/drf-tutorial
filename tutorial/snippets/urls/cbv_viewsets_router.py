from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from snippets.views.cbv_viewsets_explicitly import SnippetViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
