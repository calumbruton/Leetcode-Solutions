class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        n = abs(x)
        while n != 0 and n != -1:
            ret = ret*10 + n%10
            n = n/10
        
        # This is the max unsigned int not 2 ** 32 because we need one bit reserved as sign bit
        if(abs(ret) > (2 ** 31 - 1)): 
            return 0
        if x < 0:
            return -ret
        return ret