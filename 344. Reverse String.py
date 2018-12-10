class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


s = "A man, a plan, a canal: Panama"
test = Solution()
print(test.reverseString(s))