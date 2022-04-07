# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:59:13 2022

@author: patha
"""

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.occupied = 0
        self.store = {}

    def get(self, key: int) -> int:
        # print(self.store)
        if key in self.store.keys():
            val = self.store.pop(key)
            self.store[key] = val
            return self.store[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # print(self.store)
        if self.occupied < self.capacity and key not in self.store.keys():
            self.store[key] = value
            self.occupied += 1
        else:
            if key in self.store.keys():
                self.store.pop(key)
            else:
                self.store.pop(list(self.store.keys())[0])
            self.store[key] = value
        return None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)