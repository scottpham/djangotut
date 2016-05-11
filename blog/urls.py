from django.conf.urls import url
from . import views

# 127.0.0.1:8000
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
