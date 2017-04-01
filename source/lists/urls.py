from django.conf.urls import url

from lists.views import view_list, add_item, new_list


urlpatterns = [
    
    url(r'^(\d+)/$', view_list, name='view_list'),
    url(r'^(\d+)/add_item$', add_item, name='add_item'),
    url(r'^new$', new_list, name='new_list'),

]
