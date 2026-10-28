from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_map = {}
        for i,num in enumerate(nums):
            need_num = target - num
            if need_num in need_map:
                return (need_map[need_num],i)
            need_map[num]=i    
