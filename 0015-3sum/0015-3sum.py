class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                total = nums[i] + nums[lp] + nums[rp]
                if total == 0:
                    res.append([nums[i],nums[lp],nums[rp]])
                    lp += 1
                    rp -= 1
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp + 1]:
                        rp -= 1
                elif total < 0:
                    lp += 1
                else:
                    rp -= 1
        return res                               
        