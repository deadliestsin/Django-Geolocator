from django.conf.urls import url
from events import views

urlpatterns = [
    url(r'^event/(?P<lat>.*)/(?P<lon>.*)/(?P<rad>\d+)/(?P<count>\d+)/$', views.GetEvent.as_view()),

    url(r'^event/type/$', views.GetEventType.as_view()),
    url(r'^event/type/(?P<name>.*)/$', views.GetEventType.as_view()),
]