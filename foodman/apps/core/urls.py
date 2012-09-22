from django.conf.urls import patterns, url

urlpatterns = patterns('foodman.apps.core.views',
    url(r'^choose/$', 'choose', name='choose_foodman'),
)
