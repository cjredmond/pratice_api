
from django.conf.urls import url
from django.contrib import admin
from sample.views import PersonListCreateAPIView, PersonDetailUpdateDestroyAPIView, \
FreeAgentListCreateAPIView, FreeAgentDetailUpdateDestroyAPIView, PackersPlayerListCreateAPIView, \
PackersPlayerDetailUpdateDestroyAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/:persons/$', PersonListCreateAPIView.as_view(), name="person_list_api_view"),
    url(r'^api/:persons/(?P<pk>\d+)/$', PersonDetailUpdateDestroyAPIView.as_view(), name="person_detail_api_view"),
    url(r'^api/:free-agents/$', FreeAgentListCreateAPIView.as_view(), name="free_agents_list_api_view"),
    url(r'^api/:free-agents/(?P<pk>\d+)/$', FreeAgentDetailUpdateDestroyAPIView.as_view(), name="free_agents_detail_api_view"),
    url(r'^api/:packers-players/$', PackersPlayerListCreateAPIView.as_view(), name="packers_list_api_view"),
    url(r'^api/:packers-players/(?P<pk>\d+)/$', PackersPlayerDetailUpdateDestroyAPIView.as_view(), name="packers_detail_api_view"),
]
