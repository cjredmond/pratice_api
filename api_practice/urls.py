
from django.conf.urls import url
from django.contrib import admin
from sample.views import PersonListCreateAPIView, PersonDetailUpdateDestroyAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/:persons/$', PersonListCreateAPIView.as_view(), name="person_list_api_view"),
    url(r'^api/:persons/(?P<pk>\d+)/$', PersonDetailUpdateDestroyAPIView.as_view(), name="person_detail_api_view")
]
