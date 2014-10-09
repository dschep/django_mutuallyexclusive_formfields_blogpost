from django.conf.urls import patterns, include, url

from demo.views import V1TestView, V2TestView, V3TestView, V4TestView

urlpatterns = patterns('',
    url(r'v1', V1TestView.as_view()),
    url(r'v2', V2TestView.as_view()),
    url(r'v3', V3TestView.as_view()),
    url(r'v4', V4TestView.as_view()),
)
