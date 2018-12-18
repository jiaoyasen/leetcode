class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        path = []
        for i in image:
            tmp = []
            for j in i:
                tmp.append(False)
            path.append(tmp)
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        path[sr][sc] = True
        self.dfs(image,sr,sc,oldColor,newColor,path)
        return image

    def dfs(self, image, sr, sc, oldColor ,newColor,path):
        if  (0<=sc+1<len(image[0])) and (image[sr][sc + 1] == oldColor) and path[sr][sc + 1] is False :
            image[sr][sc + 1] = newColor
            path[sr][sc + 1] = True
            self.dfs(image, sr, sc + 1, oldColor, newColor,path)
        if   (0 <= sc - 1 < len(image[0])) and (image[sr][sc - 1] == oldColor) and path[sr][sc - 1] is False:
            image[sr][sc - 1] = newColor
            path[sr][sc - 1] = True
            self.dfs(image, sr, sc - 1, oldColor, newColor,path)
        if (0 <= sr + 1 < len(image))  and (image[sr+1][sc] == oldColor) and path[sr+1][sc] is False:
            image[sr + 1][sc] = newColor
            path[sr + 1][sc] = True
            self.dfs(image, sr + 1, sc, oldColor, newColor,path)
        if (0 <= sr -1 < len(image)) and (image[sr-1][sc] == oldColor) and path [sr-1][sc] is False:
            image[sr - 1][sc] = newColor
            path[sr - 1][sc] = True
            self.dfs(image, sr - 1, sc, oldColor, newColor,path)
        else:
            return



test = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(test.floodFill(image,sr,sc,newColor))