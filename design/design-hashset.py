class MyHashSet(object):

    def __init__(self):
        self.dict = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.dict[key] = 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.dict.pop(key, None)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return not (self.dict.get(key) is None)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
