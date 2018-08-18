from django.conf.urls import url, include

from .views import Login, Logout, List, GetNew, Edit

from django.views.decorators.csrf import csrf_exempt

administration = ([
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^list/', List.as_view(), name='list'),
    url(r'^get_new/', GetNew.as_view(), name='get_new'),
    url(r'^edit/(?P<data_id>\d+)/$', Edit.as_view(), name='edit'),

], 'administration')


urlpatterns = [
    url(r'^', include(administration, namespace="administration")),
]

