#!/usr/bin/python3
"""
BasicCache module implementing a simple dict-based caching system.

This module defines the BasicCache class, which extends the BaseCaching class.
It provides a basic caching mechanism where items
can be stored and retrieved using a key.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class implementing a simple dict-based caching system.
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key for the item.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

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
