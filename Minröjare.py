from random import randint

class Square:
    def __init__(self,x,y, bomb = False, flag = False, view = False):
        self.x = x
        self.y = y
        self.bomb = bomb
        self.flag = flag
        self.view = view


    def __str__(self):
        if self.bomb == True:
            return 'X    '
        else: return 'O    '
        # return f'({self.x}, {self.y}, {self.bomb})'
    
# class Number(Square):
#     def __init__(self, x, y):
#         super().__init__(x, y)
    
# class Bomb(Square):
#     def __init__(self, x, y):
#         super().__init__(x, y)

#The game's height and width.
gameWidth = 5
gameHeight = 5

running = True

bombPerRow = gameWidth/3

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

playGrid = makeGrid(gameWidth, gameHeight)
plantBombs(playGrid)
displayGrid(playGrid)

# while running == True:
#     userInput = input("select your square: ")
#     if userInput == "quit":
#         running = False