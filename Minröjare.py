from random import randint

class Square:
    def __init__(self,x,y, bomb = False, flag = False, view = False):
        self.x = x
        self.y = y
        self.bomb = bomb
        self.flag = flag
        self.view = view
        self.bombCount = 0

    def countBombs(self, grid): #Counts the bombs around the square with given grid
        amount = 0
        if grid[gameHeight-self.y][self.x-1].bomb == True: #return 0 if square contains a bomb
            return 0
        else: #Counts bombs
            for row in grid[max(gameHeight-self.y-1, 0):min(gameHeight-self.y+2, 5)]:
                for column in row[max(self.x-2, 0):min(self.x+1, 5)]:
                    if column.bomb == True:
                        amount += 1
        return amount
            
    def __str__(self):
        if self.bomb == True:
            return 'X    '
        else: return f'{self.bombCount}    '

#The game's height and width.
gameWidth = 5
gameHeight = 5

running = True

bombPerRow = gameWidth // 3

def makeGrid(width, height): #makes a grid with square objects, each with their own coordinate.
    return [[Square(x+1, height-y) for x in range(width)] for y in range(height)]

def displayGrid(grid): #Displays a given grid. Also prints where the X and Y axis is.
    print(f'x-values ------>', end = '')
    print('\n')
    for x in grid: #looks through all rows (x-values)
        for y in x: #looks through the columns in the rows (y-values)
            print(y, end=' ') #prints out the squareObject (calls squares __str__ to show its x, y)
        if x[-1].y == 1:
            print('^ y-values ^')
        print('\n')

def plantBombs(grid): #Plants bombs in selected grid.
    for x in grid:
        visited = []
        bombCount = 0
        for square in x:
            if randint(0, 1) == 1 and visited.count(square.x) == 0 and bombCount < bombPerRow:
                square.bomb = True
                bombCount += 1
            visited.append(square.x)

def calculateBombCounts(grid):
    for y in grid:
        for x in y:
            x.bombCount = x.countBombs(grid)

playGrid = makeGrid(gameWidth, gameHeight)
plantBombs(playGrid)
calculateBombCounts(playGrid)  # Calculate bomb counts for each square
displayGrid(playGrid)