class Solution(object):
    def twoSum(self, numbers, target):

        p1 = 0
        p2 = len(numbers)-1
        while numbers[p1]+numbers[p2] != target and p1<p2:
            val = numbers[p1]+numbers[p2]
            if val < target:
                p1 += 1
            else:
                p2 -= 1
        
        if p1 == p2:
            return None
        return [p1+1,p2+1]