class Solution(object):
    def hammingDistance(self, x, y):
        return len([x for x in (bin(x ^ y)) if x == "1"])

        