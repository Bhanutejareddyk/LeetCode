class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # new = {}
        # for idx,val in enumerate(numbers):
        #     need_num = target - val
        #     if need_num in new:
        #         return (new[need_num] + 1,idx + 1)
        #     new[val]=idx   
        lp=0
        rp=len(numbers)-1
        while lp < rp:
            total = numbers[lp] + numbers[rp]
            if total == target:
                return(lp + 1, rp + 1)
            elif total < target:
                lp += 1
            else:
                rp -= 1            
        