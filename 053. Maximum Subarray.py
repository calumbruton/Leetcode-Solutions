class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ovrl = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i]+nums[i-1])
            if nums[i] > ovrl: ovrl = nums[i]
        
        return ovrl