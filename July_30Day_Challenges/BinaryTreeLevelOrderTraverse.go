// Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

// For example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its bottom-up level order traversal as:
// [
//   [15,7],
//   [9,20],
//   [3]
// ]
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type NL struct {
	node  *TreeNode
	level int
}

func levelOrderBottom(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	ans := make([][]int, 0)
	queue := []NL{NL{root, 0}}
	cur_level := 0
	row := make([]int, 0)
	for len(queue) > 0 {
		curNL := queue[0]
		queue = queue[1:]
		curLevel := curNL.level
		if curLevel == cur_level {
			row = append(row, curNL.node.Val)
		} else {
			cur_level = curLevel
			ans = append(ans, row)
			row = make([]int, 0)
			row = append(row, curNL.node.Val)
		}
		if curNL.node.Left != nil {
			queue = append(queue, NL{curNL.node.Left, curNL.level + 1})
		}
		if curNL.node.Right != nil {
			queue = append(queue, NL{curNL.node.Right, curNL.level + 1})
		}

	}
	ans = append(ans, row)
	i, j := 0, len(ans)-1
	for i <= j {
		ans[i], ans[j] = ans[j], ans[i]
		i++
		j--
	}
	return ans
}