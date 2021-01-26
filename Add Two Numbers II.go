// You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Follow up:
// What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

// Example:

// Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 8 -> 0 -> 7
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    stack1, stack2 := make([]*ListNode,0), make([]*ListNode,0)
    for l1!=nil {
        stack1 = append(stack1,l1)
        l1 = l1.Next
    }
    for l2 != nil {
        stack2 = append(stack2,l2)
        l2 = l2.Next
    }
    if len(stack1) < len(stack2) {
        stack1, stack2 = stack2, stack1
    }
    store := stack1[0]
    carry := 0
    for len(stack1)>0 && len(stack2)>0 {
        ele1 := stack1[len(stack1)-1]
        ele2 := stack2[len(stack2)-1]
        new_total := ele1.Val + ele2.Val + carry
        ele1.Val = new_total%10
        carry = new_total/10
        stack1 = stack1[:len(stack1)-1]
        stack2 = stack2[:len(stack2)-1]
    }
    for len(stack1) > 0 {
        ele1 := stack1[len(stack1)-1]
        new_total := ele1.Val + carry
        ele1.Val = new_total%10
        carry = new_total/10
        stack1 = stack1[:len(stack1)-1]
    }
    if carry>0 {
        new_header := &ListNode{carry,store}
        return new_header
    }
    return store
}