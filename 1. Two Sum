class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        comp = {}
        for i in range (len(nums)) :
            tofind = target - nums[i]
            if tofind in comp :
                return [i, comp[tofind]]
            comp[nums[i]] = i
