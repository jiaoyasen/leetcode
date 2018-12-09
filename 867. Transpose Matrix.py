class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])
        result = []
        for i in range(n):
            col = []
            for j in range(m):
                col.append(A[j][i])
            result.append(col)
        return result

    def transpose1(self, A):
        if not A:
            return
        m = len(A[0])
        return [[A[i][j] for i in range(len(A))] for j in range(m)]

    def transpose2(self, A):
        return list(zip(*A))



test = Solution()
A = [[1,2,3],[4,5,6]]
print(test.transpose(A))