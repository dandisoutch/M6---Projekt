from random import randint

class Square:
    def __init__(self, x, y, bomb=False, flag=False, view=False):
        self.x = x
        self.y = y
        self.bomb = bomb
        self.flag = flag
        self.view = view
        self.bomb_count = 0  # Initialize bomb count

    # Displaying itself as a character
    def __str__(self):
        if self.flag == True:
            return 'F    '
        else:
            if self.bomb:
                return 'X    '  # Return 'X' if it's a bomb
            else:
                if self.bomb_count == 0:
                    return 'O    '
                else:
                    return f'{self.bomb_count}    '  # Return bomb count if it's not a bomb

def countBombs(grid, row, col):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # List of relative positions of the eight neighbors
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
        (0, -1),         (0, 1),     # Left, Right
        (1, -1), (1, 0), (1, 1)      # Bottom-left, Bottom, Bottom-right
    ]
    
    bomb_count = 0
    
    for dr, dc in neighbors:
        new_row = row + dr
        new_col = col + dc
        
        # Check boundaries to avoid index out of range 
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col].bomb:  # Check if the neighbor is a bomb
                bomb_count += 1
    
    return bomb_count

# The game's height and width.
gameWidth = 5
gameHeight = 5

bombPerRow = gameWidth // 3  # Ensure bomb count is an integer

def makeGrid(width, height):  # Makes a grid with square objects
    return [[Square(x + 1, height - y) for x in range(width)] for y in range(height)]

def displayGrid(grid):  # Displays a given grid
    print(f'x-values ------>', end='')
    print('\n')
    for x in grid:  # Looks through all rows
        for y in x:  # Looks through the columns in the rows
            print(y, end=' ')  # Prints out the squareObject
        if x[-1].y == 1:
            print('^ y-values ^')
        print('\n')

def plantBombs(grid):  # Plants bombs in selected grid
    for y in range(len(grid)):
        bombCount = 0
        for x in range(len(grid[y])):
            # Try to place bombs until the required amount is reached
            if bombCount < bombPerRow and randint(0, 1) == 1:
                if not grid[y][x].bomb:  # Only place bomb if not already placed
                    grid[y][x].bomb = True
                    bombCount += 1


## Debugging purpuses only ##
def calculateBombCounts(grid):
    rows = len(grid)
    for y in range(rows):
        for x in range(len(grid[y])):
            grid[y][x].bomb_count = countBombs(grid, y, x)  # Update bomb count for each square

playGrid = makeGrid(gameWidth, gameHeight)

plantBombs(playGrid)

displayGrid(playGrid)

## TEST FOR DISPLAYING VALUE
while True:
    selected_x = int(input("Select x value: "))
    selected_y = int(input("Select y value: "))
    playGrid[selected_x][selected_y].bomb_count = countBombs(playGrid,selected_y,selected_x)
    displayGrid(playGrid)

## TEST FOR FLAGS
# while True:
#     selected_x = int(input("Select x value: "))
#     selected_y = int(input("Select y value: "))
#     if playGrid[selected_x][selected_y].flag == True:
#         playGrid[selected_x][selected_y].flag = False
#     else:
#         playGrid[selected_x][selected_y].flag = True
#     displayGrid(playGrid)