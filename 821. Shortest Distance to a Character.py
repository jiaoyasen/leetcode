import collections
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = []
        C_index = []
        ab_list = list(S)
        for i in range(len(ab_list)):
            if ab_list[i] == C:
                C_index.append(i)
        for i in range(len(ab_list)):
            if ab_list[i] == C:
                result.append(0)
            else:
                tmp = (abs(j - i) for j in C_index)
                result.append(min(tmp))
        return result



test = Solution()
S = "loveleetcode"
C = 'e'
print(test.shortestToChar(S,C))