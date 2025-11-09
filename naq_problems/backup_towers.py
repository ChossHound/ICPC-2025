# https://naq25.kattis.com/contests/naq25/problems/backuptowers

import time

# Get grid info
[height, width, towerCt] = [int(x) for x in input().split()]

# Get tower positions
towers: list[int] = []
for i in range(towerCt):
    towers.append([int(x) for x in input().split()])

# 2d list of the closest 2 towers
distances: list[list[list[int]]] = []

# Populate `distances` with initial data
for y in range(height):
    row = []
    for x in range(width):
        row.append([])
    distances.append(row)

# Reserve a location for a specific tower at some x/y position
def reserveLocation(id: int, x: int, y: int):
    cell = distances[y][x]

    # Cell is full
    if (len(cell) >= 2):
        return False

    cell.append(id)
    return True

# Reserve some area around a tower with a given index (id - 1)
def reserveRadius(index: int, radius: int) -> bool:
    y = towers[index][0] - 1
    x = towers[index][1] - 1

    # Get x-bounds to check
    x0 = max(x - radius, 0)
    x1 = min(x + radius, width - 1)

    change = False

    # Reserve all open squares in a diamond-shaped area
    for xi in range(x0, x1 + 1):
        
        # Get distance used to get to this x-position
        dist = abs(x - xi)

        # Get amount we are allowed to move after x-offset
        offset = radius - dist

        y0 = y - offset
        y1 = y + offset

        # Check xi, y0
        if (y0 >= 0):
            change = reserveLocation(index + 1, xi, y0) or change

        # Check xi, y1
        if (y0 != y1 and y1 < height):
            change = reserveLocation(index + 1, xi, y1) or change
    
    # Track if any change happened
    return change

def printLocations(closeness: int):
    lines = []
    for row in distances:
        line = ""
        for cell in row:
            
            # Print out the `closeness`-est cell
            if (closeness < len(cell)):
                line += f"{cell[closeness]} "

            # Indicate an invalid cell
            else:
                line += "? "
        lines.append(line)

    # Note: String modification is MUCH faster than dealing with the OS flushing the terminal output
    print("\n".join(lines))

# Loop up to the max distance
for radius in range(height + width):
    
    # The elements to remove this itteration
    toRemove: list[int] = []

    for i in range(len(towers)):
        
        # No change; Finished updating
        if (not reserveRadius(i, radius)):
            toRemove.append(i)

    # Loop backwards through lsit of elements to remove
    for i in range(len(toRemove) - 1, -1, -1):
        towers.pop(toRemove[i]) # Remove towers
    
    # Out of towers to check; Finished!
    if (len(towers) == 0):
        break

printLocations(0)
printLocations(1)
