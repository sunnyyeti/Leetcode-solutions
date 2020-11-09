// Given the head of a linked list, return the list after sorting it in ascending order.

// Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

// Example 1:


// Input: head = [4,2,1,3]
// Output: [1,2,3,4]
// Example 2:


// Input: head = [-1,5,3,4,0]
// Output: [-1,0,3,4,5]
// Example 3:

// Input: head = []
// Output: []
 

// Constraints:

// The number of nodes in the list is in the range [0, 5 * 104].
// -105 <= Node.val <= 105
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func sortList(head *ListNode) *ListNode {
    length := getListLength(head)
    if length==0 || length==1 {
        return head
    }
    half := head
    for i:=0;i<length/2-1; i++ {
        half = half.Next
    }
    next := half.Next
    half.Next = nil
    first := sortList(head)
    second := sortList(next)
    return merge(first,second)
    
}
func merge(head1, head2 *ListNode) *ListNode{
    dummy := &ListNode{}
    start := dummy
    for head1!=nil && head2!=nil{
        if head1.Val < head2.Val {
            start.Next = head1
            head1 = head1.Next
        }else{
            start.Next = head2
            head2 = head2.Next
        }
        start = start.Next
    }
    if head1!=nil{
        start.Next = head1
    }
    if head2!=nil{
        start.Next = head2
    }
    return dummy.Next
    
}
func getListLength(head *ListNode) int {
    if head==nil{
        return 0
    }
    cnt := 1
    for head.Next != nil {
        cnt++
        head = head.Next
    }
    return cnt
}