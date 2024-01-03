#!/usr/bin/python3
"""
FIFOCache module implementing a First-In-First-Out (FIFO) based caching system.

This module defines the FIFOCache class, which extends the BaseCaching class.
It provides a caching mechanism where items are added to the cache,
and when the cache reaches its maximum capacity,
the oldest item is removed to make space for the new item.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class implementing a First-In-First-Out based caching system.
    """

    def __init__(self):
        """
        Initialize class instance.
        """
        super().__init__()

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

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = sorted(self.cache_data)[0]
            self.cache_data.pop(discarded_key)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key associated with the item to retrieve.

        Returns:
            The cached item if found,
            or None if the key is not present in the cache.
        """
        return self.cache_data.get(key)
