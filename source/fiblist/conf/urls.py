from django.conf.urls import include, url
from django.contrib import admin

from lists.views import home_page
from core.views import custom_server_error

# error pages
# handler400 = 'core.views.custom_bad_request'
# handler403 = 'core.views.custom_permission_denied'
# handler404 = 'core.views.custom_page_not_found'
# handler500 = 'core.views.custom_server_error'
# handler502 = 'core.views.custom_bad_gateway'

urlpatterns = [

    url(r'^$', home_page, name='home'),

    url(r'^lists/', include('lists.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^(\d)/$', custom_server_error, name='custom-server-error'),
]
