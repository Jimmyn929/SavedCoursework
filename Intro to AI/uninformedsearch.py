#!/usr/bin/env python
# coding: utf-8

# In[11]:


import queue


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
    
    start_x = int(input("Starting point (x value): "))
    start_y = int(input("Starting point (y value): "))
    start = [start_x, start_y]
      
    goal_x = int(input("Goal point (x value): "))
    goal_y = int(input("Goal point (y value): "))
    goal = [goal_x, goal_y]
    
    
    while(True):
        searchType = input("BFS or DFS? ")
        
        if searchType == 'BFS' or searchType == 'DFS':
            break;
        
        
    #BFS: searchType = 0
    #DFS: searchType = 1
    #searchType = 0
    
    #path = breadthFirstSearch(grid, start, goal)
    path = uninformedSearch(grid, start, goal, searchType)
    outputGrid(grid, start, goal, path)
    
    
    
    
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        
    
    #start = [1,1]
    #n = Node(start, '')
    #o = Node(start, n)

    
        
def getNeighbors(location, grid):
    #print("using getneighbor")
    
    neighbors = []
    
    
    
    #below
    if(grid[location[0] + 1][location[1]] == 0):
        neighbors.append([location[0] + 1, location[1]])
    
    #above
    if(grid[location[0] - 1][location[1]] == 0):
        neighbors.append([location[0] - 1, location[1]])
        
    #left
    if(grid[location[0]][location[1] - 1] == 0):
        neighbors.append([location[0], location[1] - 1])
    
    #right
    if(grid[location[0]][location[1] + 1] == 0):
        neighbors.append([location[0], location[1] + 1])
    
    
    return neighbors
    #print("done getneighbors")

    

def expandNode(location, openList, grid, closedList):
    #print("using expandnode")
    neighbor = getNeighbors(location.value, grid)
    
    
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
    


def uninformedSearch(grid, start, goal, searchType):
    current = Node(start, None) 
    openList = [current]
    closedList = []
    
    while current.value != goal and len(openList) != 0:
        #print('in while')
        
        #BFS
        if searchType == 'BFS':
            current = openList.pop(0)
        #DFS
        if searchType == 'DFS':
            current = openList.pop(len(openList) - 1)
        
        #check if current is the goal
        if(current.value == goal):
            print(current.value)
            path = []
            path = setPath(current, path)
            return path
        
        #if not goal then expand node current
        else:
            expandNode(current, openList, grid, closedList)
            closedList.append(current) 
    
Main()


# In[ ]:





# In[ ]:




