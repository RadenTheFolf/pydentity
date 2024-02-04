class Cache:
    def __init__(self):
        self._cache = {}

    def __getitem__(self, key):
        return self._cache[key]

    def __setitem__(self, key, value):
        self._cache[key] = value

    def __delitem__(self, key):
        del self._cache[key]

    def __iter__(self):
        return iter(self._cache)

    def __len__(self):
        return len(self._cache)

    def __repr__(self):
        return repr(self._cache)

    def __str__(self):
        return str(self._cache)

    def get_cache(self):
        return self._cache

    def set_cache(self, cache: dict):
        self._cache = cache

    def clear_cache(self):
        self._cache = {}

    def get_keys(self):
        return self._cache.keys()

    def get_values(self):
        return self._cache.values()

    def get_items(self):
        return self._cache.items()

    def get(self, key, default=None):
        return self._cache.get(key, default)

    def set(self, key, value):
        self._cache[key] = value

    def delete(self, key):
        del self._cache[key]

    def has_key(self, key):
        return key in self._cache

    def has_value(self, value):
        return value in self._cache.values()


