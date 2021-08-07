#!/usr/bin/env python
# coding: utf-8

# In[47]:


import random
import math

class Board():

    def __init__(self, numRowsCols):
        self.cells = [[0] * numRowsCols for i in range(numRowsCols)]
        self.numRows = numRowsCols
        self.numCols = numRowsCols

		# negative value for initial h...easy to check if it's been set or not
        self.h = -1

    # Print board
    def printBoard(self):
        for row in self.cells:
            print (row)

    # Randomize the board
    def rand(self):
        for row in self.cells:
            i = random.randint(0, self.numCols-1)
            row[i] = 1

    # Swap two locations on the board
    def swapLocs(self, a, b):
        temp = self.cells[a[0]][a[1]]
        self.cells[a[0]][a[1]] = self.cells[b[0]][b[1]]
        self.cells[b[0]][b[1]] = temp





# Cost function for a board
def numAttackingQueens(board):

    # Collect locations of all queens
    locs = []
    for r in range( len(board.cells) ):
        for c in range( len(board.cells[r]) ):
            if board.cells[r][c] == 1:
                locs.append([r, c])
    #print 'Queen locations: %s' % locs

    result = 0

    # For each queen (use the location for ease)
    for q in locs:

        # Get the list of the other queen locations
        others = [x for x in locs if x != q]
        #print 'q: %s others: %s' % (q, others)
    
        count = 0
        # For each other queen
        for o in others:
            #print 'o: %s' % o
            diff = [o[0] - q[0], o[1] - q[1]]

            # Check if queens are attacking
            if o[0] == q[0] or o[1] == q[1] or abs(diff[0]) == abs(diff[1]):
                count = count + 1

        # Add the amount for this queen
        result = result + count

    return result




# Move any queen to another square in the same column
# successors all the same                            
# getNeighbors
def getSuccessorStates(board):
    result = []

    for i_row, row in enumerate(board.cells):
        # Get the column the queen is on in this row
        # [0] because list comprehension returns a list, even if only one element
        # This line will crash if the board has not been initialized with rand() or some other method
        i_queen = [i for i,x in enumerate(row) if x == 1][0]

        # For each column in the row
        for i_col in range(board.numCols):

            # If the queen is not there
            if row[i_col] != 1:
                # Make a copy of the board
                bTemp = Board(board.numRows)
                bTemp.cells[:] = [r[:] for r in board.cells]

                # Now swap queen to i_col from i_queen
                bTemp.swapLocs([i_row, i_col], [i_row, i_queen])
                #bTemp.printBoard()
                result.append(bTemp)

    return result

#---------------------------------------------------------------------------------------------


def schedule(T, decay_rate):
    return T*decay_rate



def simulatedAnnealing(start, limit, decay):
    #print("in simulatedAnnealing")
    
    current = start
    T = 100
    
    current.h = numAttackingQueens(current)
    print("\nInital h-value:", current.h)
    
    #main loop
    while(T > 0.000001):
        
        T = schedule(T, 0.9)
        
        
        
        if T < 0.000001:
            #print("exitting simulatedAnnealing")
            print("Final h-value:", current.h)
            current.printBoard()
            return current.h
        
            
        
        successor = getSuccessorStates(current)
        next = successor[random.randrange(len(successor))]
        
        current.h = numAttackingQueens(current)
        next.h = numAttackingQueens(next)
        
        if(next.h < current.h):
            current = next
        else:
            if(random.randrange(100) < math.exp((current.h - next.h) / T)):
                current = next
        
    
def runningFunction(limit, decay, boardsize):
    hsum = 0
    
    print("T:", limit)
    print("decay rate:", decay)
    
    for x in range(10):
        
        
        print("Run #", x)
        start = Board(boardsize)
        start.rand()
        start.printBoard()
        hsum += simulatedAnnealing(start, limit, decay)
        print()
    
    print("Average h-value:", hsum/10)
    print()
    
    
    
def main():
    print("in main")
    
    boardsize = 4
    print("Board size:", boardsize)
    
    while boardsize <= 16:
        limit = 0.000001
        decay = 0.9
        runningFunction(limit, decay, boardsize)
    
        limit = 0.0000001
        decay = 0.75
        runningFunction(limit, decay, boardsize)
        
        limit = 0.00000001
        decay = 0.5
        runningFunction(limit, decay, boardsize)
        
        boardsize *= 2
        
    print("exitting main")


# In[48]:


main()


# In[ ]:




