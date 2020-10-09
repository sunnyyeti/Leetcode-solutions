// Given a binary tree root and a linked list with head as the first node. 

// Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

// In this context downward path means a path that starts at some node and goes downwards.

 

// Example 1:



// Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
// Output: true
// Explanation: Nodes in blue form a subpath in the binary Tree.  
// Example 2:



// Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
// Output: true
// Example 3:

// Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
// Output: false
// Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
 

// Constraints:

// 1 <= node.val <= 100 for each node in the linked list and binary tree.
// The given linked list will contain between 1 and 100 nodes.
// The given binary tree will contain between 1 and 2500 nodes.
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func compare(head *ListNode, root *TreeNode) bool {
    if head==nil{
        return true
    }else if root==nil || root.Val!=head.Val  {
        return false
    }else {
        return compare(head.Next,root.Left) || compare(head.Next,root.Right)
    }
}
func isSubPath(head *ListNode, root *TreeNode) bool {
    stack := []*TreeNode{root}
    for len(stack)>0 {
        curnode := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        if compare(head,curnode){
            return true
        }
        if curnode.Left != nil {
            stack = append(stack,curnode.Left)
        }
        if curnode.Right != nil {
            stack = append(stack,curnode.Right)
        }
    }
    return false
    
}