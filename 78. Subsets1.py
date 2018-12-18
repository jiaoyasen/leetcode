class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []
        self.dfs(path,0,nums,result)
        return result

    def dfs(self,path,idx,nums,result):
        result.append(path[:])
        for i in range(idx,len(nums)):
            path.append(nums[i])
            self.dfs(path,i+1,nums,result)
            path.pop()

test = Solution()
nums = [1,2,3]
print(test.subsets(nums))