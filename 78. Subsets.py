class Solution:

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        status = [0] * len(nums)
        self.robot(result,0,status,nums)
        return result
    def robot(self,result,idx,status,nums):
        result_tmp = []
        if(idx >= len(nums)):
            for i in range(len(nums)):
                if status[i] == 1:
                    result_tmp.append(nums[i])
            result.append(result_tmp)
            return
        status[idx] = 1
        self.robot(result,idx+1,status,nums)
        status[idx] = 0
        self.robot(result,idx+1,status,nums)

test = Solution()
nums = [1,2,3]
print(test.subsets(nums))

