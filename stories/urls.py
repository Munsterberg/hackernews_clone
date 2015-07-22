from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^story/$', views.story, name='story_form'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^vote/$', views.vote),
]
