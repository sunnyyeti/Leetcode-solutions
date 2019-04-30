# Design a HashMap without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

# Example:

# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1 
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found) 

# Note:

# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.
class Node(object):
    def __init__(self,key=None,val=None,pre=None,next_=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next_ = next_

class List(object):
    def __init__(self):
        self.header = Node()
        self.tail = Node()
        self.header.next_ = self.tail
        self.tail.pre = self.header

    def insert_as_last(self,node):
        last = self.tail.pre
        last.next_ = node
        self.tail.pre = node
        node.next_ = self.tail
        node.pre = last

    def insert_as_first(self,node):
        first = self.header.next_
        first.pre = node
        self.header.next_ = node
        node.next_ = first
        node.pre = self.header

    def contains_key(self,key):
        node = self.header.next_
        while node is not self.tail:
            if node.key==key:
                return node
            node = node.next_
        return None

    def remove(self,node):
        node.pre.next_ = node.next_
        node.next_.pre = node.pre
        return node

class MyHashMap(object):

        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.M = 9973
            self.bucket = [List() for i in range(self.M)]

        def put(self, key, value):
            """
            value will always be non-negative.
            :type key: int
            :type value: int
            :rtype: None
            """
            index =key%self.M
            index_list = self.bucket[index]
            find_node = index_list.contains_key(key)
            if find_node:
                find_node.val = value
            else:
                index_list.insert_as_last(Node(key,value))

        def get(self, key):
            """
            Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
            :type key: int
            :rtype: int
            """
            index = key % self.M
            index_list = self.bucket[index]
            find_node = index_list.contains_key(key)
            if find_node:
                return find_node.val
            else:
                return -1

        def remove(self, key):
            """
            Removes the mapping of the specified value key if this map contains a mapping for the key
            :type key: int
            :rtype: None
            """
            index = key % self.M
            index_list = self.bucket[index]
            find_node = index_list.contains_key(key)
            if find_node:
                index_list.remove(find_node)