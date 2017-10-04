class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        
        This could be cleaned up by putting all 3 checks into a single for loop 
        
        """
        rows = len(board)
        cols = len(board[0])

        # Check columns
        for y in range (rows):
            checkSet = set()
            for x in range (cols):
                val = board[y][x] 
                if val != '.':
                    if val in checkSet:
                        return False
                    checkSet.add(val)

        # Check rows
        for x in range (cols):
            checkSet = set()
            for y in range (rows):
                val = board[y][x] 
                if val != '.':
                    if val in checkSet:
                        return False
                    checkSet.add(val)


        # Check all 3x3 quadrants
        for n in range(rows//3):
            for i in range(cols//3):

                #For each 3x3 quadrant ensure no duplicate values
                checkSet = set()
                for x in range(3):
                    for y in range(3):
                        val = board[x+(3*n)][y+(3*i)] 
                        if val != '.':
                            if val in checkSet:
                                return False
                            checkSet.add(val)

        # Passed all tests
        return True