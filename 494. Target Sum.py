class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        result = []
        self.dfs(nums,0,result,0,S)
        return len(result)

    def dfs(self,nums,idx,count,sum,S):
        if (idx == len(nums)):
            if(sum == S):
                count.append(1)
            return
        self.dfs(nums,idx+1,count,sum+nums[idx],S)
        self.dfs(nums, idx + 1,count,sum-nums[idx],S)


nums = [1, 1, 1, 1, 1]
S = 3
test = Solution()
print(test.findTargetSumWays(nums,S))