#!/usr/bin/env python3
"""
FIFOCache class that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache caching system class"""

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Aassigns to the dictionary self.cache_data
        the item value for the key key"""

        if key is None or item is None:
            return

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            discard_key = list(self.cache_data)[0]
            self.cache_data.pop(discard_key)
            print("DISCARD: {}".format(discard_key))

        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
