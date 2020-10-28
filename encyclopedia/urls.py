from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.wiki_entry, name="wiki_entry"),
    path("search/", views.wiki_search, name="wiki_search"),
    path("/edit-entry/<title>/", views.edit_entry, name="edit_entry"),
    path("delete-entry/<title>", views.delete_entry, name="delete_entry"),
    path("create-entry/", views.create_entry, name="create_entry"),
    path("random-entry/", views.random_entry, name="random_entry"),
    path("save-entry/", views.save_entry, name="save_entry"),
    path("/wiki/page-not-found/", views.notFound, name="notfound"),
]

# urlpatterns = [
#     path("", views.index, name="index"),

#     re_path(r"^wiki/(?P<title>\w+)/$", views.wiki_entry, name="wiki_entry"),
#     path("wiki/create/", views.create_entry, name="create_entry"),
#     path("wiki/save/", views.save_entry, name="save_entry"),
#     re_path(r"^wiki(?P<search>)\w*/$", views.wiki_search, name="wiki_search"),
#     path("wiki/edit/<title>", views.edit_entry, name="edit_entry"),
#     # re_path(r"^wiki/(?P<create>)\w*/$", views.edit_entry, name="create_entry"),
#     path("wiki/page-not-found/", views.notFound, name="notfound"),
# ]
# path("wiki/<title>/", views.wiki_entry, name="wiki_entry"),
# path("wiki/create/<title>", views.edit_entry, name="edit_entry"),
