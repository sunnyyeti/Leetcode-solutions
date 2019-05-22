# ou are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_arr = [l1]
        l2_arr = [l2]
        while l1.next:
            l1 = l1.next
            l1_arr.append(l1)
        while l2.next:
            l2 = l2.next
            l2_arr.append(l2)
        if len(l1_arr) < len(l2_arr):
            l1_arr, l2_arr = l2_arr, l1_arr
        i, j = len(l1_arr) - 1, len(l2_arr) - 1
        carry = 0
        while j >= 0:
            tmp = l1_arr[i].val + l2_arr[j].val + carry
            sum_ = (tmp) % 10
            carry = tmp // 10
            l1_arr[i].val = sum_
            i -= 1
            j -= 1
        while i >= 0:
            tmp = l1_arr[i].val + carry
            sum_ = (tmp) % 10
            carry = tmp // 10
            l1_arr[i].val = sum_
            i -= 1

        if not carry:
            return l1_arr[0]
        else:
            res = ListNode(carry)
            res.next = l1_arr[0]
            return res

        l