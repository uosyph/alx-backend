#!/usr/bin/python3
"""
LRUCache module implementing a Least Recently Used (LRU) based caching system.

This module defines the LRUCache class, which extends the BaseCaching class.
It provides a caching mechanism where items are added to the cache,
and when the cache reaches its maximum capacity,
the least recently used item is removed to make space for the new item.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache class implementing a Least Recently Used based caching system.
    """

    def __init__(self):
        """
        Initialize class instance.
        """
        super().__init__()
        self.cache_data = OrderedDict()

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
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key[0]}")

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
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
