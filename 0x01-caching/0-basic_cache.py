#!/usr/bin/python3
'''inherits from BaseCaching and is a caching system'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''a caching system'''
    def __init__(self):
        '''initialize the class'''
        BaseCaching.__init__(self)

    def put(self, key, item):
        """assign to the dictionary an item"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """return the value of an item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
