class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = {}
        for x in nums:
            if x in times:
                times[x] += 1
                if times[x] > len(nums)/2:
                    return x
            else:
                times[x] = 1
                if times[x] > len(nums)/2:
                    return x