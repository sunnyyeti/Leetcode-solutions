// A binary tree is univalued if every node in the tree has the same value.

// Return true if and only if the given tree is univalued.

 

// Example 1:


// Input: [1,1,1,1,1,null,1]
// Output: true
// Example 2:


// Input: [2,2,2,5,2]
// Output: false
 

// Note:

// The number of nodes in the given tree will be in the range [1, 100].
// Each node's value will be an integer in the range [0, 99].
// Accepted

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        if (root==NULL){
            return true;
        }
        return isUnivalTreeHelper(root,root->val);
        
    }
    bool isUnivalTreeHelper(TreeNode* node, int parent_val){
        if (node==NULL){
            return true;
        }
        if (node->val!=parent_val){
            return false;
        }
        return isUnivalTreeHelper(node->left,node->val) && isUnivalTreeHelper(node->right,node->val);
    }

};