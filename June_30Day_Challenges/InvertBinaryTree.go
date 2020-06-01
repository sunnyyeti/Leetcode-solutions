// Invert a binary tree.

// Example:

// Input:

//      4
//    /   \
//   2     7
//  / \   / \
// 1   3 6   9
// Output:

//      4
//    /   \
//   7     2
//  / \   / \
// 9   6 3   1
// Trivia:
// This problem was inspired by this original tweet by Max Howell:

// Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
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
func invertTree(root *TreeNode) *TreeNode {
	// if root==nil{
	//     return root
	// }
	// invertLeft := invertTree(root.Left)
	// invertRight:= invertTree(root.Right)
	// root.Right = invertLeft
	// root.Left = invertRight
	// return root
	if root == nil {
		return root
	}
	stack := make([]*TreeNode, 0)
	stack = append(stack, root)
	for len(stack) > 0 {
		curnd := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		curnd.Left, curnd.Right = curnd.Right, curnd.Left
		if curnd.Left != nil {
			stack = append(stack, curnd.Left)
		}
		if curnd.Right != nil {
			stack = append(stack, curnd.Right)
		}
	}
	return root

}