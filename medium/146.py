class Node:
    def __init__(self, key: int, val: int) -> None:
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_to_head(node)
            node.val = value
        else:
            if len(self.cache) >= self.capacity:
                self.remove_tail()
            node = Node(key, value)
            self.add_to_head(node)
            self.cache[key] = node
    
    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_to_head(self, node: Node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node
    
    def remove_tail(self):
        if len(self.cache) == 0: return
        tail = self.tail.prev
        del self.cache[tail.key]
        self.remove_node(tail)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)