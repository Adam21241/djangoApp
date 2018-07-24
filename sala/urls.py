from django.conf.urls import url
from . import views


app_name = 'sala'

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^(?P<sala_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<sala_id>[0-9]+)/rezerwuj/$', views.rezerwuj, name='rezerwuj'),

    url(r'^(?P<sala_id>[0-9]+)/confirm/$', views.confirm, name='confirm'),


]