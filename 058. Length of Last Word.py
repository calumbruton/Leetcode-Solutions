class Solution(object):
    def lengthOfLastWord(self, s):
        """
        O(n) solution
        """
        
        i = -1
        # Remove trailing whitespace
        while abs(i)<=len(s) and s[i] == " ":
            i -= 1
        
        count = 0
        # Once we have arrived at a word count the numbers of letters it has
        while abs(i)<=len(s) and s[i] != " ":
            i -= 1
            count += 1
        
        return count
        
    
        