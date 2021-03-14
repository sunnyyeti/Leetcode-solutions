# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
# Example 3:

# Input: head = [1], k = 1
# Output: [1]
# Example 4:

# Input: head = [1,2], k = 1
# Output: [2,1]
# Example 5:

# Input: head = [1,2,3], k = 2
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        def length(node):
            l = 0
            while node.next:
                node = node.next
                l += 1
            return l
        def forward(head,steps):
            while steps:
                head = head.next
                steps -= 1
            return head
        dummy = ListNode(-1,head)
        list_length = length(dummy)
        first = forward(dummy,k-1)
        second = forward(dummy,list_length-k)
        first.next,second.next = second.next,first.next
        first.next.next,second.next.next = second.next.next, first.next.next
        return dummy.next
        
        