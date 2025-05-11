
# Tile  -   Quadrupally-Linked List of tile nodes
# MEMBER VARIABLES
#   Up, Down, Left, Right:  Reference to neighbor node(s)
#   collapsed:              Is the tile collapsed?
#   tile:                   Tile connection data + image ?
class Tile:
    def __init__(self, up=None, down=None, left=None, right=None):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

        self.collapsed = False
        self.image = 0
    
    # create_grid  -   Set up a grid of tile nodes
    # RETURNS
    #                   Single node connected to all other nodes (? maybe change to entire list)
    # PARAMETERS
    #   length, height:  Dimensions.
    def create_grid(self, length, height):
        # Create a 2D list to hold the nodes
        grid = [[Tile() for j in range(height)] for i in range(length)]
        
        for j in range(height):
            for i in range(length):

                # Connect all pointers
                if (i > 0):
                    grid[i][j].left = grid[i-1][j]
                if (i < length - 1):
                    grid[i][j].right = grid[i+1][j]
                if (j > 0):
                    grid[i][j].up = grid[i][j-1]
                if (j < height - 1):
                    grid[i][j].down = grid[i][j+1]

        return grid

    #Returns the image associated with the tile.
    def image():
        return image

    # 
    # RETURNS
    #                   Single node connected to all other nodes (? maybe change to entire list)
    # PARAMETERS
    #   data:           dict list of strings.
    def collapse():
        pass


