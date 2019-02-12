# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Example:

# root = [5,3,6,2,4,null,7]
# key = 3

    # 5
   # / \
  # 3   6
 # / \   \
# 2   4   7

# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    # 5
   # / \
  # 4   6
 # /     \
# 2       7

# Another valid answer is [5,2,6,null,4,null,7].

    # 5
   # / \
  # 2   6
   # \   \
    # 4   7
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        header = TreeNode(key-1)
        header.right = root
        found = self.search(header,key)
        if not found:
            return header.right
        if found.val<key:
            tar = found.right
        else:
            tar = found.left
        if not tar.left:
            if tar.right:
                if found.val<key:
                    found.right = tar.right
                else:
                    found.left = tar.right
            else:
                if found.val<key:
                    found.right = None
                else:
                    found.left = None
        else:
            if not tar.right:
                if found.val < key:
                    found.right =  tar.left
                else:
                    found.left = tar.left
            else:
                next_parent = self.next_key(tar)
                if next_parent.left is None:
                    next_parent.left = tar.left
                    repl = next_parent
                else:
                    repl = next_parent.left
                    next_parent.left = repl.right
                    repl.left = tar.left
                    repl.right = tar.right

                if found.val<key:
                    found.right = repl
                else:
                    found.left = repl
        return header.right



    def next_key(self, node):
        node_r = node.right
        while node_r.left and node_r.left.left:
            node_r = node_r.left
        return node_r

    def search(self, header, key):
        if not header:
            return header
        if header.val < key:
            if header.right and header.right.val==key:
                return header
            return self.search(header.right,key)
        else:
            if header.left and header.left.val == key:
                return header
            return self.search(header.left,key)    