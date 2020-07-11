// Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

// Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

// Example 1:

// Input: root = [2,3,1,3,1,null,1]
// Output: 2
// Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
// Example 2:

// Input: root = [2,1,1,1,3,null,null,null,null,null,1]
// Output: 1
// Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
// Example 3:

// Input: root = [9]
// Output: 1

// Constraints:

// The given binary tree will have between 1 and 10^5 nodes.
// Node values are digits from 1 to 9.
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isPP(arr []int) bool {
	cnt := 0
	//fmt.Println(arr)
	for _, v := range arr {
		cnt += v & 1
	}
	return cnt <= 1
}

func helper(root *TreeNode, cnt []int, count *int) {
	if root.Left == nil && root.Right == nil {
		if isPP(cnt) {
			*count++
		}
		return
	}
	if root.Left != nil {
		cnt[root.Left.Val-1]++
		helper(root.Left, cnt, count)
		cnt[root.Left.Val-1]--
	}
	if root.Right != nil {
		cnt[root.Right.Val-1]++
		helper(root.Right, cnt, count)
		cnt[root.Right.Val-1]--
	}
}
func pseudoPalindromicPaths(root *TreeNode) int {
	total := 0
	cnt := make([]int, 9)
	cnt[root.Val-1]++
	helper(root, cnt, &total)
	return total

}