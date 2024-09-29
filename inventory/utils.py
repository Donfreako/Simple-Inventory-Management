from django.core.cache import cache

def get_cache(key):
    return cache.get(key)

def set_cache(key, value, timeout=300):
    cache.set(key, value, timeout)
