#
# 题目描述:
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
# 找出那个只出现了一次的元素。
# 说明：你的算法应该具有线性时间复杂度。你可以不使用额外空间来实现吗？
#
# 解法2:使用按位异或。由于异或操作^具有如下几个性质：
# 那么，将原 nums 数组里的所有数进行按位异或，每两个相等的数都异或为 0 而抵消了，
# 最后剩下的数与 0 异或得到的是它本身，即为只出现过一次的数。


from typing import List

class Solution:
    def singleNumber(self, numbers: List[int]) -> int:
        result = 0
        for number in numbers:
            result ^= number
            return result

solution_value = Solution()
result_value = solution_value.singleNumber([1, 2, 3, 5, 2, 1])

if result_value == 0:

else:
    print(result_value)
