from django.conf.urls import patterns, include, url

from django.contrib import admin
from CarSharing_app.views import search_form, search,addCarSharingData,storeCarSharingData,register,welcome, profile, update_details, addDriverData,storeDriverData
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('CarSharing_app.views',
    url(r'^$', welcome),
    url(r'^welcome/', welcome),
    
    
    
    url(r'^profile/', profile),
    #url(r'^information/', searchPersonal),
    url(r'^update_details/', addDriverData),
    url(r'^store_details/', storeDriverData),


    
    
    
    url(r'^search/$',search),
    url(r'^search-form/$',search_form),
    url(r'^add_record/$',addCarSharingData),
    url(r'^add_wdata/$',storeCarSharingData),
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'^accounts/register/$',register),
    url(r'^accounts/profile/$',welcome),
    
)