# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be 
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        if root.left:
            if root.right:
                return "{}({})({})".format(root.val,self.serialize(root.left),self.serialize(root.right))
            else:
                return "{}({})".format(root.val,self.serialize(root.left))
        else:
            if root.right:
                return "{}()({})".format(root.val,self.serialize(root.right))
            else:
                return "{}".format(root.val)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        if "(" not in data and ")" not in data:
            return TreeNode(int(data))
        begin = data.index("(")
        val = int(data[:begin])
        node = TreeNode(val)
        cnt = 1
        for j in range(begin+1,len(data)):
            if data[j]=="(":
                cnt+=1
            elif data[j]==")":
                cnt-=1
                if cnt==0:
                    break
        node.left = self.deserialize(data[begin+1:j])
        node.right = self.deserialize(data[j+2:-1])
        return node