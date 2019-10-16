class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        color = image[sr][sc]
        height = len(image)
        width = len(image[0])
        seen = set()
        queue = [(sr,sc)]
        while (queue):
            row, col = queue.pop()
            if (image[row][col] == color):
                image[row][col] = newColor
                # Left
                if (self.valid(row,col-1,height,width)):
                    queue.append((row,col-1))
                # Right
                if (self.valid(row,col+1,height,width)):
                    queue.append((row,col+1))
                # Up
                if (self.valid(row+1,col,height,width)):
                    queue.append((row+1,col))
                # Down
                if (self.valid(row-1,col,height,width)):
                    queue.append((row-1,col))
        
        return image

    def valid(self,r,c,height,width):
        if r < 0 or r >= height or c < 0 or c >= width: 
            return False
        return True
    
    
# Cool Solution

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
        if orig_color != newColor:
            traverse(sr, sc)
        return image