from django.urls import path
from .views import *

app_name = "post"

urlpatterns = [
    # static urls
    path("index/", index_view, name="index_url"),
    path("create/", create_view, name="create_url"),

    #dynamic urls
    path("<slug:slug>/", details_view, name="details_url"),
    path("<slug:slug>/update/", update_view, name="update_url"),
    path("<slug:slug>/delete/", delete_view, name="delete_url"),

]
