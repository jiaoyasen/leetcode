class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        #my code
        J_set = set(J)
        result = 0
        for i in S:
            if i in J_set: result += 1
        return result
        #best code
        return sum([1 for stone in S if stone in J])

J = "aA"; S = "aAAbbbb"
print(Solution().numJewelsInStones(J,S))