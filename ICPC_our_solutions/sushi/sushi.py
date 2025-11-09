plates = int(input())
costs = [int(x) for x in input().split()]

costIndex = 0

nummembers, numevents = [int(x) for x in input().split()]

events: list[tuple[int, int]] = []
for i in range(numevents):
    words = input().split()

    events.append((
        int(words[0]),
        int(words[1]) # 1-index players (chef is @ 0)
    ))

# Maps player -> plate $
belt: dict[int, int] = {}

# Stores player bills
players: dict[int, int] = {}

# All players start with a tab of $0
for i in range(nummembers):
    players[i + 1] = 0

# Add new plate, and advance to next item on menu
def add_plate(blt, index):
    global costIndex

    blt[index] = costs[costIndex]
    costIndex = (costIndex + 1) % len(costs)


def step(size: int):
    if (size <= 0):
        return

    global belt

    for i in range(size):
        new_belt: dict[int, int] = {}
        
        for pos in belt:
            new_pos = (pos + 1) % (nummembers + 1)
            new_belt[new_pos] = belt[pos]

        belt = new_belt

        if (not (0 in belt)):
            add_plate(belt, 0)

add_plate(belt, 0)
curr_time = 0


for (time, player) in events:
    step(time - curr_time)
    curr_time = time

    # Remove plate from belt
    plate = belt[player]
    del belt[player]

    # Bill player
    players[player] += plate

# Print out player bills
for i in range(nummembers):
    print(players[i + 1])
