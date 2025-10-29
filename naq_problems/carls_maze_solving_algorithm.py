# https://naq25.kattis.com/contests/naq25/problems/carlsmazesolvingalgorithm

class Carl:
    
    # Coordinate system:
    # North-east corner represented by (0,0)
    x: int = 0
    y: int = 0

    dest_x: int = 0
    dest_y: int = 0

    maze: list[list[bool]] = []

    # Map of all Carl's previously visited states
    states = {}

    # Direction represented by this value.
    # "Up" is 0
    dir: 0 | 1 | 2 | 3 = 3 # Carl starts facing right (EAST)

    # Initialize Carl with some start position
    def __init__(self, x, y, dest_x, dest_y, maze):
        self.x = x
        self.y = y
        self.dest_x = dest_x
        self.dest_y = dest_y

        self.maze = maze

    def forward(self):
        self.x, self.y = self.get_coord_in_dir(0)

    def save_state(self):
        self.states[(self.x, self.y, self.dir)] = True

    def is_duplicate_state(self):
        return (self.x, self.y, self.dir) in self.states

    # Get coordinate 1 step from Carl in some direction (relative to Carl's direction)
    def get_coord_in_dir(self, dir: 0 | 1 | 2 | 3) -> tuple[int, int]:
        new_dir = (dir + self.dir) % 4

        match new_dir:
            case 0: # NORTH
                return (self.x, self.y - 1)
            case 1: # WEST
                return (self.x - 1, self.y)
            case 2: # SOUTH
                return (self.x, self.y + 1)
            case 3: # EAST
                return (self.x + 1, self.y)
        
        # Invalid direction
        return (self.x, self.y)


    # Model turning left as incrementing the 'dir' value
    def turn_left(self):
        self.dir = (self.dir + 1) % 4

    # Model turning right as decrementing the 'dir' value
    def turn_right(self):
        self.dir = (self.dir - 1) % 4

    # Check if maze is open in some location
    def is_maze_open(self, x: int, y: int) -> bool:
        if (y < 0 or y >= len(self.maze) or x < 0 or x >= len(self.maze[y])):
            return False # Invalid location
        
        return not self.maze[y][x] # Return state of maze at that location
    
    # Run one step of Carl's logic
    def step(self) -> bool:

        # Indicate that duplicate state is found
        # Exit early
        if (self.is_duplicate_state()):
            return False

        # Indicate that Carl has found his destination!
        if (self.is_at_dest()):
            return False

        # Save current position+rotation to prevent duplicates
        self.save_state()

        # If can turn left + move, do so
        if (self.is_maze_open(*self.get_coord_in_dir(1))):
            self.turn_left()
            self.forward()
            return True

        # If can turn move forward
        if (self.is_maze_open(*self.get_coord_in_dir(0))):
            self.forward()
            return True
        
        # Otherwise, turn right
        self.turn_right()
        return True

    def is_at_dest(self) -> bool:
        return self.x == self.dest_x and self.y == self.dest_y

rows, cols = [int(x) for x in input().split()]

# Get start/end coordinates
# Subtract 1 to get values indexed by 0
startY, startX = [int(x) - 1 for x in input().split()]
endY, endX = [int(x) - 1 for x in input().split()]

maze: list[list[bool]] = []
for i in range(rows):
    
    # Convert string of 0/1 chars into array of True/False bools
    row = [int(x) == 1 for x in list(input())]

    maze.append(row)

carl = Carl(startX, startY, endX, endY, maze)

# Continuously let carl run through the maze
while (carl.step()):
    pass

# Once carl finishes, print out pass/fail
if (carl.is_at_dest()):
    print(1)
else:
    print(0)
