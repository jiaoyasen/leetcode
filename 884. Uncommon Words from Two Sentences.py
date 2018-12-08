import collections
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        result = []
        a_list = A.split()
        b_list = B.split()
        a_dict = collections.Counter(a_list)
        b_dict = collections.Counter(b_list)
        for i in a_dict.keys():
            if a_dict.get(i) == 1 and i not in b_dict.keys():
                result.append(i)
        for i in b_dict.keys():
            if b_dict.get(i) == 1 and i not in a_dict.keys():
                result.append(i)
        return result



A = "apple apple"
B = "banana"
test = Solution()
print(test.uncommonFromSentences(A,B))