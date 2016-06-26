
from __future__ import absolute_import, unicode_literals

from django.conf.urls import patterns,url

from . import views

urlpatterns = patterns('',

    # Basic pages
    url(r'^$', views.index, name='index'),
    url(r'^generate_image/',views.generate_image,name='generate_image'),
    url(r'^parse_text/',views.parse_text,name='parse_text')
    
)
