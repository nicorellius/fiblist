from django.conf.urls import patterns, include, url
from django.contrib import admin

# error pages
handler400 = 'core.views.custom_bad_request'
handler403 = 'core.views.custom_permission_denied'
handler404 = 'core.views.custom_page_not_found'
handler500 = 'core.views.custom_server_error'
handler502 = 'core.views.custom_bad_gateway'

urlpatterns = patterns(
    '',

    url(r'^$', 'lists.views.home_page', name='home'),

    url(r'^lists/', include('lists.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^(\d)/$', 'core.views.custom_server_error'),
)
