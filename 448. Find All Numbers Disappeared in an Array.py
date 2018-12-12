class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set([i+1 for i in range(len(nums))]) - set(nums))

test = Solution()
nums = [4,3,2,7,8,2,3,1]
print(test.findDisappearedNumbers(nums))