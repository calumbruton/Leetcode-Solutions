class Solution(object):
    def searchMatrix(self, matrix, target):
        
        # Base Case
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return False

        # Use altered Binary Search for the correct row by checking if the target is less then the smallest
        # number in the row or larger then the highest, if neither then binary search in the row
        l = 0
        h = len(matrix)-1
        while l<=h:
            row = l+((h-l)//2)
            # If the target is less than the min value in the row make high one row lower than row
            if target < matrix[row][0]:
                h = row-1
            
            elif target > matrix[row][-1]:
                l = row+1
                
            else:
                # The target is in the range of this row
                # Now binary search this row for the target value
                s, b = 0, len(matrix[row])
                while s <= b:
                        mid = s+((b-s)//2)
                        if target == matrix[row][mid]:
                            return True
                        elif target < matrix[row][mid]:
                            b = mid-1
                        else:
                            s = mid+1
                return False
            
        
        return False
        