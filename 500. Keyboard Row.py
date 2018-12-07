class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        row1 = set(['q','w','e','r','t','y','u','i','o','p'])
        row2 = set(['a','s','d','f','g','h','j','k','l'])
        row3 = set(['z','x','c','v','b','n','m'])
        for i in words:
            s = set(i.lower())
            if s.issubset(row1) or s.issubset(row2) or s.issubset(row3):
                result.append(i)
        return result

b = ["Hello","Alaska","Dad","Peace"]
a = Solution()
print(a.findWords(b))

