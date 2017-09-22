class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n, x in enumerate(nums):
            for i,y in enumerate(nums[n+1:]):
                if x+y == target:
                    return [n,i+n+1]