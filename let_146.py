class Node(object):
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = Node(key=key, value=value)
            self.add_to_head(node)
            self.data[key] = node
            if len(self.data) > self.capacity:
                del_node = self.remove_tail()
                del self.data[del_node.key]

    def add_to_head(self, node: Node):
        old_node = self.head.next
        old_node.prev = node
        node.next = old_node
        node.prev = self.head
        self.head.next = node

    def move_to_head(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_to_head(node)

    def remove_tail(self):
        old_node = self.tail.prev
        self.tail.prev = old_node.prev
        old_node.prev.next = self.tail
        return old_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)