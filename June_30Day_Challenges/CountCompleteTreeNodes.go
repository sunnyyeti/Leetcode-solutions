// Given a complete binary tree, count the number of nodes.

// Note:

// Definition of a complete binary tree from Wikipedia:
// In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

// Example:

// Input:
//     1
//    / \
//   2   3
//  / \  /
// 4  5 6

// Output: 6
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
func countNodes(root *TreeNode) int {
	return hp(root, -1, -1)
}

func hp(root *TreeNode, lp int, rp int) int {
	if root == nil {
		return 0
	}
	if lp < 0 {
		lp = 0
		for left := root.Left; left != nil; lp++ {
			left = left.Left
		}

	}
	if rp < 0 {
		rp = 0
		for right := root.Right; right != nil; rp++ {
			right = right.Right
		}
	}
	if lp == rp {
		return 1<<(lp+1) - 1
	}
	return hp(root.Left, lp-1, -1) + hp(root.Right, -1, rp-1) + 1
}