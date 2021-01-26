// You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

// struct Node {
//   int val;
//   Node *left;
//   Node *right;
//   Node *next;
// }
// Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

// Initially, all next pointers are set to NULL.

// Follow up:

// You may only use constant extra space.
// Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

// Example 1:

// Input: root = [1,2,3,4,5,6,7]
// Output: [1,#,2,3,#,4,5,6,7,#]
// Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

// Constraints:

// The number of nodes in the given tree is less than 4096.
// -1000 <= node.val <= 1000
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
	if root == nil {
		return root
	}
	cur_level := []*Node{}
	next_level := []*Node{root}
	for len(next_level) > 0 {
		cur_level = next_level
		next_level = []*Node{}
		for i, node := range cur_level {
			if i < len(cur_level)-1 {
				node.Next = cur_level[i+1]
			} else {
				node.Next = nil
			}
			if node.Left != nil {
				next_level = append(next_level, node.Left)
				next_level = append(next_level, node.Right)
			}
		}
	}
	return root

}