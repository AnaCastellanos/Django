from django.conf.urls import URL

from . import views

utlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view())
]
