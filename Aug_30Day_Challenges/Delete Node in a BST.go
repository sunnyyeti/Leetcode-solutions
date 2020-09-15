// Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

// Basically, the deletion can be divided into two stages:

// Search for a node to remove.
// If the node is found, delete the node.
// Note: Time complexity should be O(height of tree).

// Example:

// root = [5,3,6,2,4,null,7]
// key = 3

//     5
//    / \
//   3   6
//  / \   \
// 2   4   7

// Given key to delete is 3. So we find the node with value 3 and delete it.

// One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

//     5
//    / \
//   4   6
//  /     \
// 2       7

// Another valid answer is [5,2,6,null,4,null,7].

//     5
//    / \
//   2   6
//    \   \
//     4   7
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func deleteNode(root *TreeNode, key int) *TreeNode {
    dummyRoot := &TreeNode{Val:int(^uint(0)>>1),Left:root,Right:nil}
    p,t := findPT(dummyRoot,key)
    if t == nil{
        return dummyRoot.Left
    }
    if t.Right != nil {
        cur := t.Right
        if cur.Left == nil { // leftmost
            t.Val = cur.Val
            t.Right = cur.Right
        }else{
            next:=cur.Left
            for next.Left != nil {
                cur, next = next, next.Left
            }
            t.Val = next.Val
            cur.Left = next.Right
        }
    }else if t.Left != nil {
        cur := t.Left
        if cur.Right == nil{//rightmost
            t.Val = cur.Val
            t.Left = cur.Left
        }else{
            next:=cur.Right
            for next.Right != nil {
                cur, next = next, next.Right
            }
            t.Val = next.Val
            cur.Right = next.Left
        }
        
    }else{
        if p.Left == t{
            p.Left = nil
        }else{
            p.Right = nil
        }
    }
    return dummyRoot.Left
    
}

func findPT(root *TreeNode, key int) (Parent, Target *TreeNode){
    if key < root.Val {
        if root.Left != nil && root.Left.Val == key {
            Parent = root
            Target = root.Left
        }else if root.Left != nil{
            Parent, Target =  findPT(root.Left,key)
        }
        return
    }else{
        if root.Right != nil && root.Right.Val == key {
            Parent = root
            Target = root.Right
        }else if root.Right != nil {
            Parent,Target = findPT(root.Right,key)
        }
        return
    }
}