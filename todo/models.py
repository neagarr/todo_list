from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Tag"

    def __str__(self):
        return self.name


class Task(models.Model):

    content = models.TextField()
    created_at = models.DateField()
    deadline = models.DateField()
    is_complete = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name="tags",
        blank=True
    )

    class Meta:
        ordering = ("deadline",)
        verbose_name = "Task"

    def __str__(self):
        return self.tags
