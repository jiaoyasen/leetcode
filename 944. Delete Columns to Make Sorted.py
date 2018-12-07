class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        for s in zip(*A):
            if any(s[i] > s[i+1] for i in range(len(s) - 1)):
                result += 1
        return result

