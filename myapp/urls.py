from django.conf.urls import url

from . import views

app_name='myapp'
urlpatterns = [
    url(r'^hello$', views.hello, name='hello'),
    url(r'^data$', views.by_constituency, name='by_constituency'),
]

