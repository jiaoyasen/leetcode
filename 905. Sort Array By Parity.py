import collections
import math
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key=lambda x: x % 2)
        return A

t = Solution()
A = [3,1,2,4]
print(t.sortArrayByParity(A))

