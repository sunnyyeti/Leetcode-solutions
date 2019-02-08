# Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

# The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

# The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

# Return a List of ListNode's representing the linked list parts that are formed.

# Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
# Example 1:
# Input: 
# root = [1, 2, 3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The input and each element of the output are ListNodes, not arrays.
# For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but it's string representation as a ListNode is [].
# Example 2:
# Input: 
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
# Note:

# The length of root will be in the range [0, 1000].
# Each value of a node in the input will be an integer in the range [0, 999].
# k will be an integer in the range [1, 50].

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        partitions = []
        list_length = self.get_list_length(root)
        segment_length = list_length//k
        remain_length = list_length%k
        node = root
        p = 0
        while p<k:
            p_length = segment_length+1 if remain_length else segment_length
            remain_length = remain_length-1 if remain_length else remain_length
            partitions.append(node)
            l = 1
            while l<p_length:
                node = node.next
                l+=1
            next_node = node.next if node else None
            if node:
                node.next = None
            node = next_node
            p+=1
        return partitions
            
            
    def get_list_length(self,root):
        length = 0
        while root:
            length+=1
            root = root.next
        return length