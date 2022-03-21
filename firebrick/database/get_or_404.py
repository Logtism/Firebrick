from django.db.models.query import QuerySet
from django.http import HttpResponseNotFound
from django.template.loader import render_to_string


def get_object_or_404(**kwargs):
    try:
        return self.get(**kwargs)
    except self.model.DoesNotExist:
        return HttpResponseNotFound(render_to_string(settings.ERROR_TEMPLATES[404]))


QuerySet.get_object_or_404 = get_object_or_404