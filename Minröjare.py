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
        y = self.y-1 #Translates x-y values to use them in grid[][]
        x = self.x-1
        if grid[y][x].bomb == True: #return 0 if square contains a bomb
            return 0
        else: #Counts bombs in the 8 surrounding squares (and itself)
            for row in grid[max(y-1, 0):min(y+2, height)]:
                for column in row[max(x-1, 0):min(x+2, width)]:
                    if column.bomb == True:
                        amount += 1
        return amount

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
        # return f'({self.x}, {self.y})'

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
#Make the user choose gamesize?
gameWidth = 6
gameHeight = 6

running = True

bombPerRow = gameWidth // 4

def makeGrid(width, height): #makes a grid with square objects, each with their own coordinate.
    return [[Square(x+1, y+1) for x in range(width)] for y in range(height)]

def displayGrid(grid): #Displays a given grid. Also prints where the X and Y axis is.
    print(f'x-values ------>', end = '')
    print('\n')
    for y in grid: #looks through all rows (x-values)
        for x in y: #looks through the columns in the rows (y-values)
            print(x, end=' ') #prints out the squareObject (calls squares __str__ to show its x, y)
        if y[-1].y == 1:
            print('v y-values v', end= '')
        print('\n')


#Make this more random, still has tendency to spawn bombs to the left more.
def plantBombs(grid): #Plants bombs in selected grid.
    for x in grid:
        visited = []
        bombCount = 0
        while True:
            square = x[randint(0, len(x))-1]
            if square.bomb == False and visited.count(square) != 1:
                bombCount += 1
                visited.append(square)
                square.bomb = True
            if bombCount == bombPerRow:
                break


def calculateBombCounts(grid):
    for y in grid:
        for x in y:
            x.bombCount = x.countBombs(grid, gameWidth, gameHeight)

playGrid = makeGrid(gameWidth, gameHeight)
plantBombs(playGrid)
calculateBombCounts(playGrid)  # Calculate bomb counts for each square
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