
from django.urls import path, re_path

from myweb import views

urlpatterns = [
    path('', views.elog_list),
    path('new', views.elog_create),
    path('<int:elog_id>/edit', views.elog_create),
    #path('elog/<int:log_id>', views.elog_detail),
    re_path('^(?P<log_id>\d+)/$', views.elog_detail),
]
