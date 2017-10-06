# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """O(logn) solution using binary search"""
        
        if isBadVersion(1):
            return 1

        # store the last location of good and bad versions seen these are also lower and upper bounds
        lGood = 1 #low
        lBad = n #high
        while (lBad-lGood) > 1:
            i = lGood + (lBad-lGood)/2
            print(i)
            if not isBadVersion(i):
                lGood = i
            else:
                lBad = i
        
        return lBad