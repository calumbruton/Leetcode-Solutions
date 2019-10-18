
'''
A group of farmers has some elevation data, and we’re going to help them understand how rainfall flows over their farmland.
We’ll represent the land as a two-dimensional array of altitudes and use the following model, based on the idea that water flows downhill:

If a cell’s four neighboring cells all have higher altitudes, we call this cell a sink; water collects in sinks.
Otherwise, water will flow to the neighboring cell with the lowest altitude. If a cell is not a sink, you may assume it has a unique lowest neighbor and that this neighbor will be lower than the cell.

Cells that drain into the same sink – directly or indirectly – are said to be part of the same basin.

Your challenge is to partition the map into basins. In particular, given a map of elevations, your code should partition the map into basins and output the sizes of the basins, in descending order.

Assume the elevation maps are square. Input will begin with a line with one integer, S, the height (and width) of the map. The next S lines will each contain a row of the map, each with S integers – the elevations of the S cells in the row. Some farmers have small land plots such as the examples below, while some have larger plots. However, in no case will a farmer have a plot of land larger than S = 5000.

Your code should output a space-separated list of the basin sizes, in descending order. (Trailing spaces are ignored.)

While correctness and performance are the most important parts of this problem, a human will be reading your solution, so please make an effort to submit clean, readable code. In particular, do not write code as if you were solving a problem for a competition.
'''
import sys

def main(ele_map):
    '''
    Partition the map into basins, output the sizes of the basins in descending order
    '''
    sink_locs = set()
    rows = len(ele_map)
    cols = len(ele_map[0])

    # Find the locations of all sinks, a sink is a location that is surrounded by higher elevation
    for row in range(rows):
        for col in range(cols):
            if(isBasin(ele_map, row, col, rows, cols)):
                sink_locs.add((row,col))

    print(len(sink_locs))


    sink_sizes = []
    # Non sinks will have a unique lowest neighbour
    # DFS from each sink
    # Add its larger neighbours to the queue
    for sink in sink_locs:
        sink_set = set()
        sink_set.add(sink)
        seen = set()
        sink_size = 1
        stack = [sink]
        while (stack):
            row,col = stack.pop()
            print("\nPopped:", row,col)
            seen.add((row,col))
            # Check if neighbours belong to the sink
            for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                r = row+x
                c = col+y
                if (0 <= r < rows and 0 <= c < cols and (r,c) not in seen and (r,c) not in sink_locs):
                    lowest_neighbour = lowest_adjacent(ele_map, r, c, rows, cols)
                    print("Neighbour:", r, c, "Lowest neighbour loc:", lowest_neighbour)
                    # If neighbours lowest neighbour is in this basin then
                    # Add it to the basin (sink_set) and increment size
                    if lowest_neighbour in sink_set:
                        print("Adding:", r,c)
                        stack.append((r,c))
                        sink_set.add((r,c))
                        seen.add((r,c))
                        sink_size += 1
                        print("sink size now:", sink_size)
        sink_sizes.append(sink_size)
    res = sorted(sink_sizes, reverse=True)
    print(res)
    return res
        
        
'''
Returns whether the given location on an elevation map is a sink
'''
def isBasin(ele_map, row, col, rows, cols):
    for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        r = row+x
        c = col+y
        if (0 <= r < rows and 0 <= c < cols):
            if (ele_map[r][c] < ele_map[row][col]):
                # A neighbour is lower than this cell
                return False
    return True


'''
Returns the coordinates of the lowest adjacent location around a point on the elevation map
'''
def lowest_adjacent(ele_map, row, col, rows, cols):
    lowest_val = sys.maxsize
    loc = None
    for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        r = row+x
        c = col+y
        if (0 <= r < rows and 0 <= c < cols):
            if (ele_map[r][c] < lowest_val):
                lowest_val = ele_map[r][c]
                loc = (r,c)
    return loc



ele_map = [[1,5,2],[2,4,7],[3,6,9]]
main(ele_map)

ele_map = [[1,3,2],[10,4,7],[6,5,9]]
main(ele_map)

ele_map = [[1,0,2,5,8],[2,3,4,7,9],[3,5,7,8,9],[1,2,5,4,2],[3,3,5,2,1]]
main(ele_map)

ele_map = [[0,2,1,3],[2,1,0,4],[3,3,3,3],[5,5,2,1]]
main(ele_map)

