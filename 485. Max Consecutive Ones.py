class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        O(n)
        """
        count = 0
        temp = 0
        for x in nums:
            if x == 1:
                temp += 1
            else:
                print (temp)
                if temp>count:
                    count = temp
                temp = 0
        
        return max(count,temp)