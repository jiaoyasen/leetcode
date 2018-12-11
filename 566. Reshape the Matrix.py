class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ori_r = len(nums)
        ori_c = len(nums[0])
        if ori_r * ori_c != r * c:
            return nums
        else:
            result = []
            flat_list = []
            for i in range(ori_r):
                for j in range(ori_c):
                    flat_list.append(nums[i][j])

            for p in range(r):
                tmp_list = []
                for q in range(c):
                    tmp_list.append(flat_list[p * c + q ])
                result.append(tmp_list)
            return result







nums = [
    [1,2,3],
    [4,5,6]
]
r = 3
c = 2
test = Solution()
print(test.matrixReshape(nums,r,c))