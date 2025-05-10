
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
    def create_grid(length, height):
        # Create a 2D list to hold the nodes
        grid = [[Tile(None, None, None, None) for _ in range(height)] for _ in range(length)]
        # ... connect pointers
        return grid

    def image():
        return image

    # 
    # RETURNS
    #                   Single node connected to all other nodes (? maybe change to entire list)
    # PARAMETERS
    #   data:           dict list of strings.
    def collapse():
        pass


