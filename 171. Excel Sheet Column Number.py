class Solution(object):
    def titleToNumber(self, s):
        """
        O(n) solution
        """
        num = 0
        for c in s:
            num = num*26 + ord(c)-ord("A")+1
        
        return num