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

def makeGrid(width, height):
    return [[Square(x, y) for x in range(width)] for y in range(height)]

def displayGrid(grid):
    for x in grid:
        print('\n')
        for y in x:
            print(y, end=' ')

grid = makeGrid(5, 5)

displayGrid(grid)