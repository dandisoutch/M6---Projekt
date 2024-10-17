class Square:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    


class Number(Square):
    def __init__(self, x, y):
        super().__init__(x, y)
    

class Bomb(Square):
    def __init__(self, x, y):
        super().__init__(x, y)
    

def create_grid(width, height):
    grid = []
    for y in range(height):
        grid.append([])
        for x in range(width):
            