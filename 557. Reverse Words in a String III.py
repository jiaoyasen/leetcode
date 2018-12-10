class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = s.split(" ")
        tmp1 = (i[::-1] for i in tmp)
        result = " ".join(tmp1)
        return result


s = "Let's take LeetCode contest"
test = Solution()
print(test.reverseWords(s))