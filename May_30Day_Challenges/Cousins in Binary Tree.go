// In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

// Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

// We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

// Return true if and only if the nodes corresponding to the values x and y are cousins.

// Example 1:

// Input: root = [1,2,3,4], x = 4, y = 3
// Output: false
// Example 2:

// Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
// Output: true
// Example 3:

// Input: root = [1,2,3,null,4], x = 2, y = 3
// Output: false

// Constraints:

// The number of nodes in the tree will be between 2 and 100.
// Each node has a unique integer value from 1 to 100.
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func find(root *TreeNode, val, curdepth int) (int, int, bool) {
	if root.Left != nil {
		if root.Left.Val == val {
			return root.Val, curdepth + 1, true
		} else if p, d, ok := find(root.Left, val, curdepth+1); ok {
			return p, d, ok
		}
	}
	if root.Right != nil {
		if root.Right.Val == val {
			return root.Val, curdepth + 1, true
		} else if p, d, ok := find(root.Right, val, curdepth+1); ok {
			return p, d, ok
		}
	}
	return -1, -1, false
}
func isCousins(root *TreeNode, x int, y int) bool {
	if root.Val == x || root.Val == y {
		return false
	}
	xp, xd, _ := find(root, x, 0)
	yp, yd, _ := find(root, y, 0)
	return xp != yp && xd == yd
}