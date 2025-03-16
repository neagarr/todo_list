
class QuerysetMixin:
    def get_queryset_mixin(self, queryset):
        title = self.request.GET.get("title")
        if title:
            if "username" in self.model.__dict__.keys():
                return queryset.filter(username__icontains=title)
            elif "name" in self.model.__dict__.keys():
                return queryset.filter(name__icontains=title)
        return queryset
