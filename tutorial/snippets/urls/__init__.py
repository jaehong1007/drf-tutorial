from django.conf.urls import url, include

from . import fbv, cbv, cbv_mixins, cbv_generics

urlpatterns = [
    url(r'^fbv/', include(fbv, namespace='fbv')),
    url(r'^cbv/', include(cbv, namespace='cbv')),
    url(r'^cbv_mixins/', include(cbv_mixins, namespace='cbv_mixins')),
    url(r'^cbv_generics/', include(cbv_generics, namespace='cbv_mixins')),
]

