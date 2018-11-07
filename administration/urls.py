from django.conf.urls import url, include, re_path

from .views import Login, Logout, List, GetNew, Edit, TagView, SearchView
# from .views import Delete

from django.views.decorators.csrf import csrf_exempt

administration = ([
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^list/', List.as_view(), name='list'),
    url(r'^search/', SearchView.as_view(), name='search'),
    url(r'^get_new/', GetNew.as_view(), name='get_new'),
    url(r'^edit/(?P<file_name>[a-zA-Z0-9\-\.\_\s]+)/$', Edit.as_view(), name='edit'),
    url(r'^add-tag/', TagView.as_view(), name='add-tag'),
    # url(r'^delete/(?P<pk>\d+)/$', Delete.as_view(), name='delete'),

], 'administration')


urlpatterns = [
    url(r'^', include(administration, namespace="administration")),
]

