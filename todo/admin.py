from django.contrib import admin
from todo.models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("is_complete", "deadline", "tags", "content")
    list_filter = ("is_complete", "deadline", "tags")
    search_fields = ("tags", "is_complete")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
