from django.conf.urls import patterns, include, url

from django.contrib import admin
from posts.views import welcome
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weather.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', welcome),
    url(r'^welcome/', welcome),
    
    

                          
)
