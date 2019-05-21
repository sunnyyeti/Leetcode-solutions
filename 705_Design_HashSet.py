# Design a HashSet without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

# Example:

# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)

# Note:

# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
class Node(object):
    def __init__(self,val=None,pre=None,next=None):
        self.val = val
        self.pre = pre
        self.next = next

class List(object):
    def __init__(self):
        self.header = Node()
        self.tail = Node()
        self.header.next = self.tail
        self.tail.pre = self.header

    def insert_as_last(self,node):
        last = self.tail.pre
        last.next = node
        self.tail.pre = node
        node.next = self.tail
        node.pre = last

    def insert_as_first(self,node):
        first = self.header.next
        first.pre = node
        self.header.next = node
        node.next = first
        node.pre = self.header

    def contains_val(self,val):
        node = self.header.next
        while node is not self.tail:
            if node.val==val:
                return node
            node = node.next
        return None

    def remove(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre
        return node

class MyHashSet(object):

        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.M = 9973
            self.bucket = [List() for i in range(self.M)]

        def add(self, key):
            """
            :type key: int
            :rtype: None
            """
            index = key%self.M
            val_list = self.bucket[index]
            if not val_list.contains_val(key):
                val_list.insert_as_last(Node(key))


        def remove(self, key):
            """
            :type key: int
            :rtype: None
            """
            index = key%self.M
            val_list = self.bucket[index]
            find_node = val_list.contains_val(key)
            if find_node:
                val_list.remove(find_node)

        def contains(self, key):
            """
            Returns true if this set contains the specified element
            :type key: int
            :rtype: bool
            """
            index = key%self.M
            val_list = self.bucket[index]
            return bool(val_list.contains_val(key))