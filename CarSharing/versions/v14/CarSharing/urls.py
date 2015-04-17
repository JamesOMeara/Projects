from django.conf.urls import patterns, include, url

from django.contrib import admin
from CarSharing_app.views import create_message, store_message, searchUser, searchUserForm, search_form, search,addCarSharingData,storeCarSharingData,register,welcome,search_to, profile, update_details, addDriverData,storeDriverData, message_error, storeDriverCarData, addDriverCarData, About, info_journey, decrease, increase

from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('CarSharing_app.views',
    url(r'^$', welcome),
    url(r'^welcome/', welcome),
    
    
    
    url(r'^profile/', profile),
    url(r'^update_details/', addDriverData),
    url(r'^store_details/', storeDriverData),
    
    url(r'^add_car/', addDriverCarData),
    url(r'^store_car_details/', storeDriverCarData),
    
    url(r'^messanger/', create_message),
    url(r'^message_error/', message_error),
    url(r'^store_message/', store_message),


    
    url(r'^searchUserForm/$',searchUserForm),
    url(r'^searchUser/$',searchUser),
    url(r'^search/$',search),
    url(r'^search_to/$',search_to),
    url(r'^search-form/$',search_form),
    url(r'^search_journey/$',search),
    url(r'^info_journey/$',info_journey),
    
    
    url(r'^decrease/$',decrease),
    url(r'^increase/$',increase),
    
    
    url(r'^add_record/$',addCarSharingData),
    url(r'^add_wdata/$',storeCarSharingData),
    




    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout, {'next_page': '/welcome/'}),
    url(r'^accounts/register/$',register),
    url(r'^accounts/profile/$',profile),
    url(r'^About/$',About),
    
)