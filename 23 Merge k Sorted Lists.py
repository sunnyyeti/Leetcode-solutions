# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ListNode.__lt__ = lambda self, other: self.val<other.val
        k = len(lists)
        if k==0:
            return None
        if k==1:
            return lists[0]
        head = ListNode(-1,None)
        store = head
        heap = [(ln.val,ln) for ln in lists if ln]
        heapq.heapify(heap)
        while heap:
            cur_node_val, cur_node = heapq.heappop(heap)
            head.next = cur_node
            next_node = cur_node.next
            if next_node:
                heapq.heappush(heap,(next_node.val,next_node))
            head = head.next
        return store.next
        
        