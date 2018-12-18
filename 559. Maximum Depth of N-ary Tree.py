"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        depth_tmp = 0
        depth = self.getDepth(root)
        return depth

    def getDepth(self,node):
        if node is None:
            return 0
        d_tmp = 0
        for i in node.children:
            d = self.getDepth(i)
            if d > d_tmp:
                d_tmp = d
        return 1+d_tmp





test = Solution()
print(test.maxDepth())