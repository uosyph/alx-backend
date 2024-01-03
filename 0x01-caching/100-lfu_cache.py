#!/usr/bin/python3
"""
LFUCache module implementing a Least Frequently Used based caching system.

This module defines the LFUCache class, which extends the BaseCaching class.
It provides a caching mechanism where items are added to the cache,
and when the cache reaches its maximum capacity,
the least frequently used item is removed to make space for the new item.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class implementing a Least Frequently Used based caching system.
    """

    def __init__(self):
        """
        Initialize class instance.
        """
        super().__init__()
        self.keys = []
        self.uses = {}

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
            if (
                len(self.keys) == BaseCaching.MAX_ITEMS
                and key not in self.keys
            ):
                discarded_key = self.keys.pop(
                    self.keys.index(self.get_lfu_item()
                                    ))
                del self.cache_data[discarded_key]
                del self.uses[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.uses[key] += 1
            else:
                self.keys.append(key)
                self.uses[key] = 0

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
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.uses[key] += 1
            return self.cache_data[key]

    def get_lfu_item(self):
        """
        Return the key of the least frequently used item in the cache.
        If multiple items have the same usage frequency,
        return the least recently used one.

        Returns:
            The key of the least frequently used item in the cache.
        """
        items = list(self.uses.items())
        min_freq = min(self.uses.values())

        lfu_keys = [key for key, freq in items if freq == min_freq]

        for key in self.keys:
            if key in lfu_keys:
                return key
