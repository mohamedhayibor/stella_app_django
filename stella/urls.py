from django.conf.urls import url,include,patterns
from django.contrib import admin




urlpatterns = patterns(
     '',
    # ... URLs
    
    url(r'', include('stella_app.urls')),


   

)