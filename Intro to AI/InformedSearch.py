#!/usr/bin/env python
# coding: utf-8

# In[17]:


import queue
import heapq

expandCount = 0

# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1 
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of 1s and 0s
def readGrid(filename):
    #print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])
    
    f.close()
    #print 'Exiting readGrid'
    return grid


# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1 
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, path):
    #print('In outputGrid')
    filenameStr = 'path.txt'

    # Open filename
    f = open(filenameStr, 'w')

    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path)-1:
            grid[p[0]][p[1]] = '*'

    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            
            # Don't add a ' ' at the end of a line
            if c < len(row)-1:
                f.write(str(col)+' ')
            else:
                f.write(str(col))

        # Don't add a '\n' after the last line
        if r < len(grid)-1:
            f.write("\n")

    # Close file
    f.close()
    #print('Exiting outputGrid')
    
    
    
def Main():
    grid = readGrid('grid.txt')
    print(grid)      
    
    #Greedy Search: searchType = 0
    #A*: searchType = 1
    searchType = 1
    
    start = [0, 0]
    goal = [9, 9]
    
    global expandCount
    
    #path = breadthFirstSearch(grid, start, goal)
    path = informedSearch(grid, start, goal, searchType)
    outputGrid(grid, start, goal, path)
    
    
    
    
class Node:
    def __init__(self, value, parent, g, h, f):
        self.value = value
        self.parent = parent
        self.g = g  #path cost
        self.h = h  #heuristic cost
        self.f = f  #A*
        
    
    def __lt__(self, other):
        if other.f == -1:
            return self.h < other.h
        else:
            return self.f < other.f

    
        
def getNeighbors(location, grid):
    #print('In getNeighbors')
    result = []
    # Use location[:] to get a copy of the list    
    # For each direction (u,r,d,l), check the bounds and value on the grid    
    # Clockwise order -> u, r, d, l    
    
    up = location[:]    
    up[0] -= 1    
    if up[0] > -1 and grid[up[0]][up[1]] != 0:        
        result.append(up)    
        
    right = location[:]    
    right[1] += 1    
    if right[1] < len(grid[right[0]]) and grid[right[0]][right[1]] != 0:
        result.append(right)    
        
    down = location[:]    
    down[0] += 1    
    if down[0] < len(grid) and grid[down[0]][down[1]] != 0:        
        result.append(down)    
        
    left = location[:]    
    left[1] -= 1    
    if left[1] > -1 and grid[left[0]][left[1]] != 0:        
        result.append(left)    
        
    #print('Exiting getNeighbors')    
    return result
    #print("done getneighbors")

    

def expandNode(location, openList, grid, closedList, goal, searchType):
    #print("using expandnode")
    neighbor = getNeighbors(location.value, grid)
    global expandCount
    
    
    for x in neighbor:
        #Greedy Search
        if searchType == 0:
            currentNode = Node(x, location, grid[x[0]][x[1]], heuristic(x, goal), -1)
            
            if any(y.value == x for y in openList) == False and any(y.value == x for y in closedList) == False:
                heapq.heappush(openList, currentNode)
                expandCount += 1
                
        #A* search
        if searchType == 1:
            currentNode = Node(x, location, grid[x[0]][x[1]], heuristic(x, goal), grid[x[0]][x[1]] + heuristic(x, goal))
            
            if any(y.value == x for y in openList) == True:
                newG = currentNode.g
                oldG = 0
                for y in openList:
                    if y.value == x:
                        oldG = y.g
                    
                        if newG < oldG:
                            openList.remove(x)
                            heapq.heappush(openList, currentNode)
                        
                            if any(y.value == x for y in closedList) == True:
                                closedList.remove(y)
                        break
            
            elif any(y.value == x for y in closedList) == False:
                heapq.heappush(openList, currentNode)
                expandCount += 1
    
    #put node into closedlist or openlist depending on explored or not
    for x in neighbor:
        if any(i.value == x for i in openList) == False and any(i.value == x for i in closedList) == False:
            openList.append(Node(x, location))
            
    
    #print("done expandnode")
 


def setPath(current, path):
    while current.parent != None:
        path.append(current.value)
        current = current.parent
    path.append(current.value)
    
    
    return path
    
    


import math
def heuristic(node, goal):
    return math.sqrt(((goal[1] - node[1]) ** 2) + ((goal[0] - node[0]) ** 2))




def informedSearch(grid, start, goal, searchType):
    #current = Node(start, None)
    #current.g = 0
    #current.h = heuristic(current, goal)
    #current.setF()
    
    if searchType == 1:
        current = Node(start, None, grid[start[0]][start[1]], heuristic(start, goal), grid[start[0]][start[1]] + heuristic(start, goal))
    else:
        current = Node(start, None, grid[start[0]][start[1]], heuristic(start, goal), -1)
        

        
    
    openList = [current]
    closedList = []
    
    
    while current.value != goal and len(openList) != 0:
        #print('in while')
        
        current = heapq.heappop(openList)
        #print(current.value)
        
        #check if current is the goal
        if(current.value == goal):
            
            closedList.append(current)
            print(current.value)
            path = []
            path = setPath(current, path)
            print("Path Found")
            print(path)
            print("states expanded: ", expandCount)
            print("Heuristics used: Distance Formula")
            return path
        
        #if not goal then expand node current
        else:
            expandNode(current, openList, grid, closedList, goal, searchType)
            closedList.append(current) 
    
Main()


# In[ ]:





# In[ ]:




