// Find the sum of all left leaves in a given binary tree.

// Example:

//     3
//    / \
//   9  20
//     /  \
//    15   7

// There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */



func sumOfLeftLeaves(root *TreeNode) int {
    if root==nil{
        return 0
    }
    res := 0
    help(root,false,&res)
    return res
}

func help(node *TreeNode, isLeft bool, res *int) {
    if node.Left==nil && node.Right==nil && isLeft {
        *res += node.Val
    }
    if node.Left!=nil{
        help(node.Left,true,res)
    }
    if node.Right != nil {
        help(node.Right,false,res)
    }
}