class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """Least Recently Used (LRU) Cache implementation."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev = node.prev
        new_next = node.next
        prev.next = new_next
        new_next.prev = prev

    def _add(self, node: Node):
        # Always insert at the head (most recently used)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._add(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the tail node (least recently used)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print("Get 1:", cache.get(1))    # returns 1
    cache.put(3, 3)                  # evicts key 2
    print("Get 2:", cache.get(2))    # returns -1 (not found)
    cache.put(4, 4)                  # evicts key 1
    print("Get 1:", cache.get(1))    # returns -1 (not found)
    print("Get 3:", cache.get(3))    # returns 3
    print("Get 4:", cache.get(4))    # returns 4