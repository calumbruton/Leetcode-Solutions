class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)-1
        for i, dig in enumerate(reversed(digits)):
            # If the digit does not equal 9 then increase it by 1
            if dig!=9:
                digits[n-i] += 1
                return digits
            
            # If we are at largest digit and it is a 9 make it 0 and add a 1 to head of list
            elif i == n:
                digits[n-i] = 0
                digits.insert(0,1)
                return digits
            
            # If values a 9 make it 0
            else: 
                digits[n-i] = 0
                
                
                
            