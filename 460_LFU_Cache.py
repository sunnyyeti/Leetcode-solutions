# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LFUCache cache = new LFUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
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


class LFUCache:

    def __init__(self, capacity: 'int'):
        self.cap = capacity
        self.cache = {} #{key:[node,cnt,value]}
        self.lru = {} #{cnt:List}
        self.minf = None

    def get(self, key: 'int') -> 'int':
        if key not in self.cache:
            return -1
        node,cnt,value = self.cache[key]
        self.lru[cnt].remove_node(node)
        self.lru.setdefault(cnt+1,DoubleLinkedList()).insert_as_first(node)
        self.cache[key][1] = cnt+1
        if self.lru[cnt].cnt==0 and self.minf==cnt: ## current min_frequency_nodes are exhausted, then min_f in incremented by 1
            self.minf = cnt+1
        return value

    def check_capacity(self):
        if len(self.cache)<self.cap:
            return
        removed_node = self.lru[self.minf].remove_node(self.lru[self.minf].last_node)
        removed_key = removed_node.key
        self.cache.pop(removed_key)
        ##no need to find minf here, because a new node will be immediately inserted and minf will become 1

    def put(self, key: 'int', value: 'int') -> 'None':
        if self.cap==0:
            return
        if key in self.cache:
            node,cnt,_ = self.cache[key]
            self.lru[cnt].remove_node(node)
            self.lru.setdefault(cnt+1,DoubleLinkedList()).insert_as_first(node)
            self.cache[key][1] = cnt+1
            self.cache[key][2] = value
            if self.lru[cnt].cnt == 0 and self.minf == cnt:  ## current min_frequency_nodes are exhausted, then min_f in incremented by 1
                self.minf = cnt + 1
            return
        self.check_capacity()
        node = Node(key)
        self.cache[key] =[node,1,value]
        self.lru.setdefault(1,DoubleLinkedList()).insert_as_first(node)
        self.minf = 1