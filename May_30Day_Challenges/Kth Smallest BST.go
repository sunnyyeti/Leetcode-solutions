// Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

// Example 1:

// Input: root = [3,1,4,null,2], k = 1
//    3
//   / \
//  1   4
//   \
//    2
// Output: 1
// Example 2:

// Input: root = [5,3,6,2,4,null,null,1], k = 3
//        5
//       / \
//      3   6
//     / \
//    2   4
//   /
//  1
// Output: 3
// Follow up:
// What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

// Constraints:

// The number of elements of the BST is between 1 to 10^4.
// You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func helper(root *TreeNode, k int) (total_or_target int, ok bool) {
	if root == nil {
		return 0, false
	} else {
		if tt, ok := helper(root.Left, k); ok {
			return tt, true
		} else {
			if tt == k-1 {
				return root.Val, true
			} else {
				if rtt, rok := helper(root.Right, k-tt-1); rok {
					return rtt, true
				} else {
					return rtt + tt + 1, false
				}
			}
		}
	}
}
func kthSmallest(root *TreeNode, k int) int {
	t, _ := helper(root, k)
	return t
}