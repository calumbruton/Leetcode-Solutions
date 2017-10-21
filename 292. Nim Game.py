class Solution(object):
    def canWinNim(self, n):
        """
        1,2,3 - Win
        4 - False 
        5 - True
        6 - True
        7 - True
        8 - False
        
        This pattern repeats and thus is an easy 1 line O(1) solution
        """
        return False if n % 4 == 0 else True

