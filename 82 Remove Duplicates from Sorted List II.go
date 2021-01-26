// Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

// Example 1:


// Input: head = [1,2,3,3,4,4,5]
// Output: [1,2,5]
// Example 2:


// Input: head = [1,1,1,2,3]
// Output: [2,3]
 

// Constraints:

// The number of nodes in the list is in the range [0, 300].
// -100 <= Node.val <= 100
// The list is guaranteed to be sorted in ascending order.
// Accepted
// 308.4K
// Submissions
// 791.1K
// Seen this question in a real interview before?
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    dummy := &ListNode{0,nil}
    store := dummy
    for head!=nil{
        if isDuplicated(head) {
            head = skipDuplicates(head)
        }else{
            dummy.Next = head
            dummy = dummy.Next
            head = head.Next
        }
    }
    dummy.Next = nil
    return store.Next
}

func isDuplicated(node *ListNode) bool {
    return !(node.Next==nil || node.Val != node.Next.Val)
}

func skipDuplicates(node *ListNode) *ListNode {
    curVal := node.Val
    for node.Val==curVal{
        node = node.Next
        if node==nil{
            return nil
        }
    }
    return node
}