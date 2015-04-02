from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from websites.content import views
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     # url(r'^contact/$','websites.content.views.contact'),
)

if settings.REGISTER: 
    urlpatterns += patterns('',
        url(r'^accounts/login/$','django.contrib.auth.views.login', {'template_name': 'login.html'}),
        url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'template_name':'logout.html'}),
        url(r'^accounts/register/$','websites.content.views.register'),        
    )

if settings.SHOPPING:
    urlpatterns += patterns('',
        url(r'^section/(?P<section_url>\w+)/$','websites.shopping.views.section'),
        url(r'^detail/(?P<item_id>\d+)/$','websites.shopping.views.detail'),
    )

if settings.TWITTER: 
    urlpatterns += patterns('',
        url(r'^authorize/', 'websites.content.views.authorize_twitter'),
        url(r'^tlogin/','websites.content.views.twitter_login'),
    )

if settings.LANDING: 
    urlpatterns += patterns('', 
        url(r'^$', 'django.views.generic.simple.direct_to_template', {'template':'landing.html'}), 
        url(r'^home/$', views.index)
    )

#if settings.TRADITIONAL:
#    urlpatterns += patterns()

else: 
    urlpatterns += patterns('',
        url(r'^$', views.index)
    )

# if settings.DEBUG:
#     urlpatterns += patterns('',
#         (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': "/Users/ball6862/Github/Sites/django_apps/media/jakore/", 'show_indexes':True}),
# )
