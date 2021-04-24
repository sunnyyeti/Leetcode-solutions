// You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

// Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:

// Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

// Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].

// Example 1:

// Input: root = [1,2], voyage = [2,1]
// Output: [-1]
// Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.
// Example 2:

// Input: root = [1,2,3], voyage = [1,3,2]
// Output: [1]
// Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.
// Example 3:

// Input: root = [1,2,3], voyage = [1,2,3]
// Output: []
// Explanation: The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.

// Constraints:

// The number of nodes in the tree is n.
// n == voyage.length
// 1 <= n <= 100
// 1 <= Node.val, voyage[i] <= n
// All the values in the tree are unique.
// All the values in voyage are unique.
// Accepted
// 29,345
// Submissions
// 58,561
// Seen this question in a real interview before?

// Yes

// No

// Problems

// Pick One

// Prev

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func flipMatchVoyage(root *TreeNode, voyage []int) []int {
	ans := []int{}
	if root.Val != voyage[0] {
		return []int{-1}
	} else {
		flips, _ := helper(root, voyage, 0, &ans)
		if !flips {
			return []int{-1}
		} else {
			return ans
		}
	}
}

func helper(node *TreeNode, voyage []int, start int, ans *[]int) (flips bool, cnt int) {
	flips = true
	cnt = 1
	if node.Left == nil && node.Right == nil {
		return
	} else if node.Left != nil && node.Right == nil {
		if node.Left.Val == voyage[start+1] {
			lFlips, lCnt := helper(node.Left, voyage, start+1, ans)
			if lFlips == false {
				flips = false
				return
			}
			cnt += lCnt
			return
		} else {
			flips = false
			return
		}
	} else if node.Left == nil && node.Right != nil {
		if node.Right.Val == voyage[start+1] {
			rFlips, rCnt := helper(node.Right, voyage, start+1, ans)
			if rFlips == false {
				flips = false
				return
			}
			cnt += rCnt
			return
		} else {
			flips = false
			return
		}
	} else {
		if node.Left.Val == voyage[start+1] {
			lFlips, lCnt := helper(node.Left, voyage, start+1, ans)
			if lFlips == false {
				flips = false
				return
			}
			cnt += lCnt
			if node.Right.Val == voyage[start+lCnt+1] {
				rFlips, rCnt := helper(node.Right, voyage, start+lCnt+1, ans)
				if rFlips == false {
					flips = false
					return
				}
				cnt += rCnt
				return
			} else {
				flips = false
				return
			}
		} else if node.Right.Val == voyage[start+1] {
			*ans = append(*ans, node.Val)
			rFlips, rCnt := helper(node.Right, voyage, start+1, ans)
			if rFlips == false {
				flips = false
				return
			}
			cnt += rCnt
			if node.Left.Val == voyage[start+rCnt+1] {
				lFlips, lCnt := helper(node.Left, voyage, start+rCnt+1, ans)
				if lFlips == false {
					flips = false
					return
				}
				cnt += lCnt
				return
			} else {
				flips = false
				return
			}
		} else {
			flips = false
			return
		}
	}
}
