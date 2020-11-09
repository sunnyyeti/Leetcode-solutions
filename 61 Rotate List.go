// Given a linked list, rotate the list to the right by k places, where k is non-negative.

// Example 1:

// Input: 1->2->3->4->5->NULL, k = 2
// Output: 4->5->1->2->3->NULL
// Explanation:
// rotate 1 steps to the right: 5->1->2->3->4->NULL
// rotate 2 steps to the right: 4->5->1->2->3->NULL
// Example 2:

// Input: 0->1->2->NULL, k = 4
// Output: 2->0->1->NULL
// Explanation:
// rotate 1 steps to the right: 2->0->1->NULL
// rotate 2 steps to the right: 1->2->0->NULL
// rotate 3 steps to the right: 0->1->2->NULL
// rotate 4 steps to the right: 2->0->1->NULL
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
    length := getListLength(head)
    if length == 0{
        return head
    }
    k = k%length
    if k==0{
        return head
    }
    p1 := head
    p2 := p1
    for i:=0; i<k; i++ {
        p2 = p2.Next
    }
    for p2.Next != nil {
        p1 = p1.Next
        p2 = p2.Next
    }
    newHead := p1.Next
    p1.Next = nil
    p2.Next = head
    return newHead
}

func getListLength(head *ListNode) int {
    if head == nil {
        return 0
    }
    length := 1
    for head.Next != nil {
        length++
        head = head.Next
    }
    return length
}