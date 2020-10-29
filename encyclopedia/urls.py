from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.wiki_entry, name="wiki_entry"),
    re_path(r"^wiki/(?P<title>).*[\s\w]*/$", views.wiki_entry, name="wiki_entry"),
    path("search/", views.wiki_search, name="wiki_search"),
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
    path("delete-entry/<title>", views.delete_entry, name="delete_entry"),
    path("random-entry/", views.random_entry, name="random_entry"),
    path("wiki/page-not-found/", views.notFound, name="notfound"),
]
