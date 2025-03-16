
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm, TagForm
from .mixins import QuerysetMixin, ContextMixin
from .models import Task, Tag


class TaskListView(
    QuerysetMixin,
    ContextMixin,
    generic.ListView
):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "task_list"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        return self.get_context_data_mixin(context)

    def get_queryset(self):
        queryset = Task.objects.select_related("tags")
        return self.get_queryset_mixin(queryset)


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    template_name = "todo/task_form.html"
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    template_name = "todo/task_form.html"
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
    template_name = "todo/task_confirm_delete.html"


class TagListView(
    QuerysetMixin,
    ContextMixin,
    generic.ListView
):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tag_list"
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        return self.get_context_data_mixin(context)


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