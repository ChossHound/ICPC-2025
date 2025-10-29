# https://naq25.kattis.com/contests/naq25/problems/curling

# The marker to which everything is compared
button_x = 144
button_y = 84

red_score = 0
yellow_score = 0

def compute_distances(coords):
    dists = []

    for i in range(0, len(coords), 2):
        
        # Get deltas of x/y coords from button
        dx = button_x - coords[i]
        dy = button_y - coords[i + 1]

        # Compute square of distances (x^2 + y^2)
        dists.append(dx*dx + dy*dy)
    
    return dists

def compute_score(main_dists, opponent_dists) -> int:

    # Edge case: no opponent pucks on the board
    # ALL main's pucks considered "closer" than blue's
    if (len(opponent_dists) == 0):
        return len(main_dists)

    score: int = 0
    
    for dist in main_dists:

        # Opponent's score is better; Stop checking!
        if (opponent_dists[0] < dist):
            continue

        # main's stone is closer; Increment their score
        score += 1

    return score

# Loop for 10 frames
for i in range(10):
    
    # Get x, y, x, y, ...
    red_coords = [int(x) for x in input().split()[1:]]
    yellow_coords = [int(x) for x in input().split()[1:]]

    # Parse into distances
    red_dists = compute_distances(red_coords)
    yellow_dists = compute_distances(yellow_coords)

    # Sort distances
    red_dists.sort()
    yellow_dists.sort()

    # Edge case: no blue pucks on the board
    # ALL red's pucks considered "closer" than blue's
    if (len(yellow_dists) == 0):
        red_score += len(red_dists)
        continue

    red_score += compute_score(red_dists, yellow_dists)
    yellow_score += compute_score(yellow_dists, red_dists)

print(f"{red_score} {yellow_score}")