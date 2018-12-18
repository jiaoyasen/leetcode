# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        result1 = []
        self.dfs(root1,result1)
        result2 = []
        self.dfs(root2,result2)
        if result1 == result2:
            return True
        else:
            return False

    def dfs(self,root,result):
        if root.left is None and root.right is None:
            result.append(root.val)
            return
        elif root.left is not None and root.right is None:
            self.dfs(root.left, result)
        elif root.left is None and root.right is not None:
            self.dfs(root.right,result)
        else:
            self.dfs(root.left, result)
            self.dfs(root.right, result)

test = Solution()
root1 = TreeNode(1)
root2 = TreeNode(1)
print(test.leafSimilar(root1,root2))
