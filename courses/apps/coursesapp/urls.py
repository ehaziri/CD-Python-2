from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create, name="create"),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name="destroy"),
    url(r'^add_comment/(?P<id>\d+)$', views.add_comment, name="add_comment"),
    url(r'^show_comments/(?P<id>\d+)$', views.show_comments, name="show_comments")
]
