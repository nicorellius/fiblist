from django.conf.urls import patterns, include, url

# error pages
handler400 = 'common.views.custom_bad_request'
handler403 = 'common.views.custom_permission_denied'
handler404 = 'common.views.custom_page_not_found'
handler500 = 'common.views.custom_server_error'
handler502 = 'common.views.custom_bad_gateway'

urlpatterns = patterns(
    '',

    url(r'^$', 'lists.views.home_page', name='home'),

    url(r'^lists/', include('lists.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
