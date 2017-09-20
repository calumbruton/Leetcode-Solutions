class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            # increment first 2 values, from there add to i if the number is greater then that in the index 2
            # below it
            if count < 2 or n > nums[count-2]:
                nums[count] = n
                count += 1
        return count

        