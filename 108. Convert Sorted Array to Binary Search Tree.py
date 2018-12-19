# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.dfs(nums,0,len(nums)-1)
        return root
    def dfs(self,nums,start,end):
        root = None
        if end >= start:
            mid = int((start + end +1 )/2)
            root = TreeNode(nums[mid])
            root.left = self.dfs(nums,start,mid-1)
            root.right = self.dfs(nums,mid+1,end)
        else:
            root = None
        return root