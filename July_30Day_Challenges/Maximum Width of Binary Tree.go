// Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

// The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

// Example 1:

// Input: 

//            1
//          /   \
//         3     2
//        / \     \  
//       5   3     9 

// Output: 4
// Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
// Example 2:

// Input: 

//           1
//          /  
//         3    
//        / \       
//       5   3     

// Output: 2
// Explanation: The maximum width existing in the third level with the length 2 (5,3).
// Example 3:

// Input: 

//           1
//          / \
//         3   2 
//        /        
//       5      

// Output: 2
// Explanation: The maximum width existing in the second level with the length 2 (3,2).
// Example 4:

// Input: 

//           1
//          / \
//         3   2
//        /     \  
//       5       9 
//      /         \
//     6           7
// Output: 8
// Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


// Note: Answer will in the range of 32-bit signed integer.
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 type ExtTreeNode struct{
    *TreeNode
    Pos int
    Level int
}
func widthOfBinaryTree(root *TreeNode) int {
    queue := []ExtTreeNode{{root,0,0}}
    maxWidth := -1
    levelWidth := -1
    curLevel := -1
    levelStart := -1
    for len(queue)>0{
        curNode := queue[0]
        queue = queue[1:]
        if curNode.Level !=  curLevel{
            curLevel = curNode.Level
            if levelWidth > maxWidth{
                maxWidth = levelWidth
            }
            levelStart = curNode.Pos
            levelWidth = curNode.Pos-levelStart+1

        }else{
            levelWidth = curNode.Pos-levelStart+1
        }
        if curNode.Left != nil{
                queue = append(queue,ExtTreeNode{curNode.Left,2*curNode.Pos+1,curNode.Level+1})
            }
        if curNode.Right!=nil{
                queue = append(queue,ExtTreeNode{curNode.Right,2*curNode.Pos+2,curNode.Level+1})
            }
    }
    if levelWidth>maxWidth{
        return levelWidth
    }
    return maxWidth
}