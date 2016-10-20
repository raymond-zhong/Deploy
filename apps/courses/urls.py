from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^confirmdelete/(?P<id>\d+)$', views.confirmDelete),
    url(r'^delete$', views.delete),
    url(r'^viewcomments/(?P<id>\d+)$', views.viewcomments),
    url(r'^createcomment$', views.createcomment)

]
