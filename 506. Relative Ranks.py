class Solution(object):
    def findRelativeRanks(self, nums):
        # rank max 3 numbers 
        order = sorted(nums, reverse=True)
        medals =["Gold Medal","Silver Medal","Bronze Medal"]
        
        for i,num in enumerate(nums):
            loc = order.index(num)
            print(loc)
            if loc in [0,1,2]:
                nums[i] = medals[loc]
            else:
                nums[i] = str(loc+1)
                
        return nums
        