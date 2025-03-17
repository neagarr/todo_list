import requests.sessions
from django.http import HttpResponseRedirect, HttpRequest, request
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from poetry.console.commands import self

from .forms import TaskForm, TagForm
from .mixins import QuerysetMixin
from .models import Task, Tag


class TaskListView(
    QuerysetMixin,
    generic.ListView
):
    model = Task
    context_object_name = "task_list"
    paginate_by = 2


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:task_list")
    template_name = "todo/task_form.html"
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task_list")
    template_name = "todo/task_form.html"
    form_class = TaskForm
    print(HttpRequest.__dict__)


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task_list")
    template_name = "todo/task_confirm_delete.html"


class TagListView(
    QuerysetMixin,
    generic.ListView
):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tag_list"
    paginate_by = 2


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("todo:tag_list")
    template_name = "todo/tag_form.html"
    form_class = TagForm


class TagUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("todo:tag_list")
    template_name = "todo/tag_form.html"
    form_class = TagForm


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag_list")
    template_name = "todo/tag_confirm_delete.html"


class TaskCompleteToggleView(View):
    def post(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Task, id=pk)
        task.is_complete = not task.is_complete
        task.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", reverse_lazy("todo:task_list")))
