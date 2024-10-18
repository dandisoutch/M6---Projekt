class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'
    
class Number(Square):
    def __init__(self, x, y):
        super().__init__(x, y)
    
class Bomb(Square):
    def __init__(self, x, y):
        super().__init__(x, y)

#The game's height and width.
gameWidth = 5
gameHeight = 5

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

grid = makeGrid(gameWidth, gameHeight)

displayGrid(grid)