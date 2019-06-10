from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    url('^$', get_posts, name = "get_posts"),
    url('^(?P<pk>\d+)/$', post_detail, name = "post_detail"),
    url('^new/$', create_or_edit_post, name = "new_post"),
    url('^(?P<pk>\d+)/edit/$', create_or_edit_post, name = "edit_post"),
    ]