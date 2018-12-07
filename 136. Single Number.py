import collections
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = collections.Counter(nums)
        for i in a.keys():
            if a.get(i) == 1:
                return i

#best solution
        result=0
        for i in nums:
            result ^= i
        return result