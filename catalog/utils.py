from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_categories_from_cache():

    if settings.CACHE_ENABLED:
        key = 'categories'
        cache_data = cache.get(key)
        if cache_data is None:
            queryset = Category.objects.all()
            cache_data = queryset
            cache.set(key, cache_data)
        queryset = cache_data
    else:
        queryset = Category.objects.all()

    return queryset