class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lp=0
        rp=len(numbers)-1
        while lp < rp:
            total = numbers[lp] + numbers[rp]
            if total == target:
                return [lp + 1,rp + 1]
            elif total < target:
                lp += 1
            else:
                rp -= 1        
        