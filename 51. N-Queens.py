class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        path = [-1] * n
        hang = [False] * n
        fan = [False] * (n*2)
        zheng = [False] * (n*2)
        result = []
        self.dfs(result,path,hang,fan,zheng,0,n)
        return result

    def dfs(self,result,path,hang,fan,zheng,idx,n):
        if idx >= n:
            tmp_result = []
            for i in range(n):
                tmp_str = ""
                for j in range(n):
                    if j == path[i]:
                        tmp_str += 'Q'
                    else:
                        tmp_str += '.'
                tmp_result.append(tmp_str)
            result.append(tmp_result)
            return

        for i in range(n):
            if hang[i] is False and zheng[idx + i] is False and fan [idx - i + n -1] is False:
                path[idx] = i
                hang[i] = True
                zheng[idx + i] = True
                fan[idx - i + n -1] = True
                self.dfs(result,path,hang,fan,zheng,idx+1,n)
                path[idx] = -1
                hang[i] = False
                zheng[idx + i] = False
                fan[idx - i + n -1 ] = False



test = Solution()
n = 4
print(test.solveNQueens(n))