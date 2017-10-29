class Solution(object):
    def climbStairs(self, n):
        """DP Solution
        The number of ways to get to the next stair is equal to the sum of ways to get to the 2 stairs before it
        There is 1 way to get to the first stair, 2 ways to the second, therefore (1+2) ways to the third and so on..
        """
        
        steps = [1,2]
        for i in range(n-2):
            steps.append(steps[-2]+steps[-1])
        
        return steps[n-1]
            
        