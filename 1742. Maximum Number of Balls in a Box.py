class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        locs = [0 for _ in range(100)]
        for i in range(lowLimit, highLimit + 1):
            val = self.sumParts(i)
            locs[val] += 1
        return max(locs)

    def sumParts(self, num):
        ans = 0
        remainder = num
        while remainder != 0:
            ans += remainder % 10
            remainder = remainder // 10
        return ans