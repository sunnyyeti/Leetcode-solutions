# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class Node:
    def __init__(self,key=None,pre=None,next=None):
        self.key = key
        self.pre = pre
        self.next = next
class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cnt = 0

    def insert_as_first(self,node):
        firstnode = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next=firstnode
        firstnode.pre = node
        self.cnt+=1

    def insert_as_last(self,node):
        lastnode = self.tail.pre
        node.next = self.tail
        self.tail.pre = node
        node.pre = lastnode
        lastnode.next =node
        self.cnt+=1

    def remove_node(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.cnt-=1
        return node

    @property
    def last_node(self):
        if self.cnt:
            return self.tail.pre
        return None

    @property
    def first_node(self):
        if self.cnt:
            return self.head.next
        return None

class LRUCache:

    def __init__(self, capacity: 'int'):
        self.cap = capacity
        self.cache = {}
        self.list = DoubleLinkedList()

    def get(self, key: 'int') -> 'int':
        if key not in self.cache:
            return -1
        node,value = self.cache[key]
        self.list.remove_node(node)
        self.list.insert_as_first(node)
        return value

    def check_capacity(self):
        if len(self.cache)<self.cap:
            return
        removed_node = self.list.remove_node(self.list.last_node)
        key = removed_node.key
        self.cache.pop(key)

    def put(self, key: 'int', value: 'int') -> 'None':
        if key in self.cache:
            self.cache[key][1] = value
            node = self.cache[key][0]
            self.list.remove_node(node)
            self.list.insert_as_first(node)
            return
        self.check_capacity()
        node = Node(key)
        self.cache[key] = [node,value]
        self.list.insert_as_first(node)