class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in A:
            i.reverse()
            for j in range(len(i)):
                i[j] ^= 1
        return(A)