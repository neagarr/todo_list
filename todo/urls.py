from django.urls import path
from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)


urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),

    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task_update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete"
    ),

    path(
        "tags/",
        TagListView.as_view(),
        name="tag_list"
    ),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag_update"
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag_delete"
    ),

]

app_name = "manager"
