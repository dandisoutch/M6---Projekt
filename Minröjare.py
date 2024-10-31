from random import randint

class Square:
    def __init__(self,x,y, bomb = False, flag = False, view = False):
        self.x = x
        self.y = y
        self.bomb = bomb
        self.flag = flag
        self.view = view
        self.bombCount = 0

    def countBombs(self, grid, width, height): #Counts the bombs around the square with given grid
        amount = 0
        y = self.y-1 #Translates x-y values to use them in grid
        x = self.x-1
        if grid[y][x].bomb == True: #return 0 if square contains a bomb
            return 0
        else: #Counts bombs in the 8 surrounding squares (and itself)
            for row in grid[max(y-1, 0):min(y+2, height)]:
                for column in row[max(x-1, 0):min(x+2, width)]:
                    if column.bomb == True:
                        amount += 1
        return amount
    
    #This function checks for empty squares (squares with 0 bombcount)
    #around the selected square, and calls upon the same function on those squares.
    #This reveals big areas if there's a lot of empty squares.
    def emptySquares(self, grid, width, height):
        y = self.y-1
        x = self.x-1
        grid[y][x].view = True
        if grid[y][x].bombCount == 0 and grid[y][x].bomb == False:
            for row in grid[max(y-1, 0):min(y+2, height)]:
                for column in row[max(x-1, 0):min(x+2, width)]:
                    if column.view == False and column.bomb == False:
                        column.emptySquares(grid, width, height)
                        
            
    def __str__(self):
        #This function is what a square will show if you print it out.
        if self.flag and not self.view:
            return 'F    '
        else:
            if self.view:
                if self.bomb == True:
                    return 'X    '
                else: return f'{self.bombCount}    '
            else:
                return '*    '

#The game's height and width.
gameWidth = 6
gameHeight = 6

running = True

bombPerRow = gameWidth // 4 #how many bombs there are per row.

def makeGrid(width, height): #makes a grid with square objects, each with their own coordinate.
    return [[Square(x+1, y+1) for x in range(width)] for y in range(height)]

def displayGrid(grid): #Displays a given grid. Also prints where the X and Y axis is.
    print(f'x-values ------>', end = '')
    print('\n')
    for y in grid: #looks through all rows
        for x in y: #looks through the columns (the squares in the rows)
            print(x, end=' ') #prints out the squareObject
        if y[-1].y == 1:
            print('v y-values v', end= '')
        print('\n')

def plantBombs(grid): #Randomly plants bombs in selected grid.
    for y in grid: #looks through rows (list)
        bombCount = 0
        while True:
            square = y[randint(0, len(y))-1] #randomly selects a square in the row
            if square.bomb == False: #Check if there's already a bomb there
                bombCount += 1
                square.bomb = True
            if bombCount == bombPerRow:
                break


def calculateBombCounts(grid): #loops through the grid and updates the squares bombcount
    for y in grid:
        for x in y:
            x.bombCount = x.countBombs(grid, gameWidth, gameHeight)

playGrid = makeGrid(gameWidth, gameHeight)
plantBombs(playGrid)
calculateBombCounts(playGrid)
displayGrid(playGrid)

while True:
    option = input("Type F for flag or Q to quit: ").lower()

    if option == "q":
        break

    try:
        y = int(input("\ny: ")) -1
        x = int(input("x: ")) -1
        
        if option == "f":
            playGrid[y][x].flag = not playGrid[y][x].flag
        else:
            playGrid[y][x].emptySquares(playGrid, gameWidth, gameHeight)
    except(ValueError):
        print("\nNot a valid option\n")

    displayGrid(playGrid)