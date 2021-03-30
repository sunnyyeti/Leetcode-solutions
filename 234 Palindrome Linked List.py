# Given the head of a singly linked list, return true if it is a palindrome.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True
        l = self.length(head)
        #print(l)
        h = l//2
        p2 = head
        r = l-h
        #print(l,h)
        while r:
            p2 = p2.next
            r -=1 
        p1 = self.reverse(head,h-1)
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1,p2 = p1.next,p2.next
        return True
    
    def reverse(self,head,h):
        next_ = head.next
        while h:
            tmp = next_.next
            next_.next = head
            head = next_
            next_ = tmp
            h -= 1
        return head
        
    def length(self,head):
        ans = 0
        while head:
            ans += 1
            head = head.next
        return ans