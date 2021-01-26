// Given a singly linked list L: L0→L1→…→Ln-1→Ln,
// reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

// You may not modify the values in the list's nodes, only nodes itself may be changed.

// Example 1:

// Given 1->2->3->4, reorder it to 1->4->2->3.
// Example 2:

// Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    if head==nil {
        return 
    }
    nodes := make([]*ListNode,0)
    dh := head
    for dh!=nil{
        nodes = append(nodes,dh)
        dh = dh.Next
    }
    start, end := 0, len(nodes)-1
    for start < end {
        nodes[start].Next = nodes[end]
        start++
        nodes[end].Next = nodes[start]
        end--
    }
    nodes[start].Next = nil
}