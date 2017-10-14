class Solution(object):
    def rob(self, nums):
        """
        Dynamic programming O(n) solution
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        copy = [x for x in nums]
        if len(nums) > 2:
            for i in range(len(nums)-1, 1, -1):
                print(i)
                total_2steps = nums[i-2] + copy[i]
                if total_2steps > copy[i-2]:
                    copy[i-2] = nums[i-2] + copy[i]

                total_3steps = nums[i-3] + copy[i]
                if total_3steps > copy[i-3]:
                    copy[i-3] = nums[i-3] + copy[i]

        return max(copy[0],copy[1])