from django.urls import path, re_path

from django.conf.urls import handler400, handler403, handler404, handler500
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.wiki_entry, name="wiki_entry"),
    re_path(r"^wiki/(?P<title>).*[\s\w]*/$", views.wiki_entry, name="wiki_entry"),
    path("search/", views.wiki_search, name="wiki_search"),
    re_path(r"^wiki/(?P<search>).*[\w]*$", views.wiki_search, name="wiki_search"),
    re_path(
        r"^update-entry/$",
        views.update_entry,
        name="update_entry",
    ),
    re_path(
        r"^update-entry/?:/(?P<title>[a-zA-Z1-9]+)/$",
        views.update_entry,
        name="update_entry",
    ),
    # path("error/404/", views.test404, name="404"),
    path("delete-entry/<title>", views.delete_entry, name="delete_entry"),
    path("random-entry/", views.random_entry, name="random_entry"),
    re_path(r"^page-not-found/$", views.notFound, name="notFound"),
    # re_path(r"^wiki/page-not-found/$", views.notFound, name="notFound"),
]

# handler500 = "encyclopedia.views.handler_500"
