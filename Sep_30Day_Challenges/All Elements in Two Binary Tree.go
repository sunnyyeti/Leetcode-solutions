// Given two binary search trees root1 and root2.

// Return a list containing all the integers from both trees sorted in ascending order.

// Example 1:

// Input: root1 = [2,1,4], root2 = [1,0,3]
// Output: [0,1,1,2,3,4]
// Example 2:

// Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
// Output: [-10,0,0,1,2,5,7,10]
// Example 3:

// Input: root1 = [], root2 = [5,1,7,0,2]
// Output: [0,1,2,5,7]
// Example 4:

// Input: root1 = [0,-10,10], root2 = []
// Output: [-10,0,10]
// Example 5:

// Input: root1 = [1,null,8], root2 = [8,1]
// Output: [1,1,8,8]

// Constraints:

// Each tree has at most 5000 nodes.
// Each node's value is between [-10^5, 10^5].
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
	pot1 := pot(root1)
	pot2 := pot(root2)
	i, j := 0, 0
	res := []int{}
	for i < len(pot1) && j < len(pot2) {
		if pot1[i] < pot2[j] {
			res = append(res, pot1[i])
			i++
		} else {
			res = append(res, pot2[j])
			j++
		}
	}
	for ; i < len(pot1); i++ {
		res = append(res, pot1[i])
	}
	for ; j < len(pot2); j++ {
		res = append(res, pot2[j])
	}
	return res

}

func pot(root *TreeNode) []int {
	res := []int{}
	stack := make([]*TreeNode, 0)
	node := root
	for node != nil {
		stack = append(stack, node)
		node = node.Left
	}
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		res = append(res, cur.Val)
		node := cur.Right
		for node != nil {
			stack = append(stack, node)
			node = node.Left
		}
	}
	return res
}