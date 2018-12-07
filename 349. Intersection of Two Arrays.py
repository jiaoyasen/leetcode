class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))

a = Solution()
b = [4,9,5]
c = [9,4,9,8,4]
print(a.intersection(b,c))