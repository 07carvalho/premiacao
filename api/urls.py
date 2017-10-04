from django.conf.urls import url #include
from django.contrib import admin #auth

from .views import pages, award

urlpatterns = [

    url(r'^api/vote/$', award.set_user_response, name='set_user_response'),


    url(r'^$', pages.home, name='home_page'),
    url(r'^vote/$', pages.vote, name='vote_page'),
]