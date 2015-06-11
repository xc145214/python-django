from django.conf.urls import patterns, include, url
from django.contrib import admin

#import view
from views import home_page,hello,current_datetime,hours_ahead


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # home
    ('^$', home_page),

    # hello
    ('^hello/$', hello),

    # time
    ('^time/$', current_datetime),

    #another url
    ('^another-time-page/$', current_datetime),

    #
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
)
