#
#题目描述:
#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。
#找出那个只出现了一次的元素。
#说明：你的算法应该具有线性时间复杂度。你可以不使用额外空间来实现吗？
#

#
#解题思路:
#法1:
#使用字典 dict 存储每一个整数出现的次数，如果当前数在 dict 中不存在，则添加之，出现的次数设置成1，
#否则每再出现一次，次数加1。最后从里面挑出第一个出现次数为1的 KeyValuePair 的 Key 值即可。
#

from typing import List

class Solution:
    def singleNumber(self, numbers: List[int]) -> int:
        result = 0
        map = dict()
        for number in numbers:
            if number not in map:
                map[number] = 1
            else:
                map[number] += 1
        result = next(k for k, val in map.items() if val == 1)
        return result

solution_value = Solution()
print(solution_value.singleNumber([1, 2, 5, 6, 2, 5, 1, 9]))
#6

