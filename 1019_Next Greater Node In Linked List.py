# We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.
#
# Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.
#
# Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).
#
# Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.
#
#
#
# Example 1:
#
# Input: [2,1,5]
# Output: [5,5,0]
# Example 2:
#
# Input: [2,7,4,3,5]
# Output: [7,0,5,5,0]
# Example 3:
#
# Input: [1,7,5,1,9,2,5,1]
# Output: [7,9,9,9,0,5,0,0]
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head is None:
            return []
        head.pre = None
        cur = head.next
        while cur is not None:
            cur.pre = head
            head = cur
            cur = cur.next
        ans = []
        max_node = ListNode(float("inf"))
        head.nextlarger = max_node
        ans.append(0)
        pre = head.pre
        while pre:
            if pre.val<head.val:
                pre.nextlarger = head
                ans.append(head.val)
            else:
                next_larger_node = head.nextlarger
                while next_larger_node.val<=pre.val:
                    next_larger_node = next_larger_node.nextlarger
                pre.nextlarger = next_larger_node
                if next_larger_node is max_node:
                    ans.append(0)
                else:
                    ans.append(next_larger_node.val)
            head = pre
            pre = head.pre
        return ans[::-1]

