#!/usr/bin/python3
"""
MRUCache module implementing a Most Recently Used (MRU) based caching system.

This module defines the MRUCache class, which extends the BaseCaching class.
It provides a caching mechanism where items are added to the cache,
and when the cache reaches its maximum capacity,
the most recently used item is removed to make space for the new item.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCache class implementing a Most Recently Used based caching system.
    """

    def __init__(self):
        """
        Initialize class instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru = ""

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the item.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key and item:
            if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                self.mru = key
            else:
                if key not in self.cache_data:
                    discarded_key = self.mru
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")
                    self.cache_data[key] = item
                    self.mru = key
                else:
                    self.cache_data.update({key: item})
                    self.mru = key

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key associated with the item to retrieve.

        Returns:
            The cached item if found,
            or None if the key is not present in the cache.
        """
        if key in self.cache_data:
            self.mru = key
            return self.cache_data[key]
