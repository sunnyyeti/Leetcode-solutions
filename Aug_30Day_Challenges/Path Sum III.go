// You are given a binary tree in which each node contains an integer value.

// Find the number of paths that sum to a given value.

// The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

// The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

// Example:

// root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

//       10
//      /  \
//     5   -3
//    / \    \
//   3   2   11
//  / \   \
// 3  -2   1

// Return 3. The paths that sum to 8 are:

// 1.  5 -> 3
// 2.  5 -> 2 -> 1
// 3. -3 -> 11
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, sum int) int {
    if root == nil {
        return 0
    }
    cnt := 0
    helper(root,&cnt,sum)
    return cnt
    
}

func helper(node *TreeNode, cnt *int, tar int) map[int]int{
    var leftcnt, rightcnt map[int]int
    if node.Left != nil {
        leftcnt = helper(node.Left, cnt, tar)
    }
    if node.Right != nil {
        rightcnt = helper(node.Right,cnt, tar)
    }
    curnodesum := make(map[int]int)
    curnodesum[node.Val] = 1
    for k,v := range leftcnt {
        curnodesum[k+node.Val]+=v
    }
    for k,v := range rightcnt {
        curnodesum[k+node.Val]+=v
    }
    for k,v := range curnodesum {
        if k==tar {
            *cnt += v
        }
    }
    //fmt.Println("curnode",node.Val)
    //fmt.Println(curnodesum)
    return curnodesum
}