from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^sth', 'news.views.index'),
	url(r'^(?P<page>[0-9]+)/$', 'news.views.news_list', name='news-list'),
	url(r'^/?$', 'news.views.news_list', name='news-list'),
)
