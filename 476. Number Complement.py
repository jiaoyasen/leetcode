class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 0
        i = 0
        while num > 0:
            t = not (num % 2)
            num = num // 2
            n += t * 2 ** i
            i += 1
        return n


a = 5
test = Solution()
print(test.findComplement(a))