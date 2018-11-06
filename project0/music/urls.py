from django.conf.urls import url
from . import views   # HERE '.' is used for same  directory
from django.urls import re_path 

app_name = 'music'
urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view() , name='index'),

    url(r'^register/$', views.UserFormView.as_view() , name='register'),
 
    # here , "^" sign is used for "begging" AND  "$" sign is used for "ending".
    # /music/<music.id>/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    # /music/album/add/
    url(r'album/add/$',views.AlbumCreate.as_view() , name='album-add'),

    # /music/album/2/
    re_path(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view() , name='album-update'),

    # /music/album/2/delete/
    re_path(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view() , name='album-delete'),
    
]


