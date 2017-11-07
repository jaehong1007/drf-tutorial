from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ..views.cbv_mixins import UserList, UserDetail

urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^(?P<pk>\d+)/$', UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

