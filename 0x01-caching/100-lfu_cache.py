#!/usr/bin/env python3
"""
LFUCache class that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFUCache caching system class"""

    def __init__(self):
        """Initialization"""
        super().__init__()
        self.__cache_usage = {}

    def put(self, key, item):
        """Aassigns to the dictionary self.cache_data
        the item value for the key key"""

        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.__cache_usage[key] += 1
            del self.cache_data[key]
            self.cache_data[key] = item
            return

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            discard_key = min(self.__cache_usage,
                              key=self.__cache_usage.get)
            similar = {key: value
                       for key, value in self.cache_data.items()
                       if value == self.__cache_usage[discard_key]}
            if len(similar) > 1:
                discard_key = similar.keys[0]
            self.cache_data.pop(discard_key)
            self.__cache_usage.pop(discard_key)
            print("DISCARD: {}".format(discard_key))

        self.cache_data[key] = item
        self.__cache_usage[key] = 0

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        if key in self.__cache_usage.keys():
            self.__cache_usage[key] += 1
        return self.cache_data.get(key, None)
