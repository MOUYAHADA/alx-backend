#!/usr/bin/env python3
"""
a class BasicCache that inherits from
BaseCaching and is a caching system
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """Put cache data"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get cache data"""
        return self.cache_data.get(key, None)
