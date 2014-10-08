from django.conf.urls import patterns, include, url

from v1_rawdjango.views import TestView as V1TestView
from v2_djangoandjs.views import TestView as V2TestView
from v3_mutuallyexclusive_formfields.views import TestView as V3TestView
from v4_fileorurl.views import TestView as V4TestView

urlpatterns = patterns('',
    url(r'v1', V1TestView.as_view()),
    url(r'v2', V2TestView.as_view()),
    url(r'v3', V3TestView.as_view()),
    url(r'v4', V4TestView.as_view()),
)
