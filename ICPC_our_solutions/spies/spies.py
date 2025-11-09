[numTeams, numTurns] = [int(x) for x in input().split()]

# In the form [E -> W]
rows = {}

# In the form [N -> S]
cols = {}

# In the form { x,y, xi, yi, alive }
spies = []    

for i in range(numTeams):
    [x, y] = [int(x) for x in input().split()]

    # Make sure we have a place to put our guys
    if not (x in cols):
        cols[x] = []
    if not (y in rows):
        rows[y] = []

    cols[x].append((y, i))
    rows[y].append((x, i))

    spies.append({
        "x": x,
        "y": y,
        "alive": True,
        "xi": -1,
        "yi": -1
    })

def cmp(entry):
    return entry[0]

for rowId in rows:
    row: list[int, int] = rows[rowId]
    row.sort(key=cmp)

    # entry is (x, spy index)
    for i, entry in enumerate(row):
        spies[entry[1]]["xi"] = i

for colId in cols:
    col: list[int, int] = cols[colId]
    col.sort(key=cmp)

    # entry is (y, spy index)
    for i, entry in enumerate(col):
        spies[entry[1]]["yi"] = i

def eliminateBefore(arr, index, key: str) -> list[str]:
    eliminated = []

    for i in range(index - 1, -1, -1):
        entry = arr[i] # (pos, spy)
        spyIndex = entry[1]
        spy = spies[spyIndex]

        if (not spy["alive"]):
            continue

        spy["alive"] = False
        eliminated.append(spyIndex)

    # Remove dead spies
    del arr[0:index]

    for (i, entry) in enumerate(arr):
        spyIndex = entry[1]
        spy = spies[spyIndex]

        spy[key] = i

    # print("BEFORE: searched", index)
    
    return [str(spyIndex + 1) for spyIndex in eliminated]

def eliminateAfter(arr, index) -> list[str]:
    eliminated = []

    for i in range(index + 1, len(arr)):
        entry = arr[i] # (pos, spy)
        spyIndex = entry[1]
        spy = spies[spyIndex]

        if (not spy["alive"]):
            continue

        spy["alive"] = False
        eliminated.append(str(spyIndex + 1))

    # Remove dead spies
    del arr[index+1:]

    # print("AFTER: searched", len(arr) - index - 1)
    
    return eliminated

outLines = []

for i in range(numTurns):
    args = input().split() # id, direction

    spyId = int(args[0]) - 1 # Spy index is spy id - 1
    dir = args[1]

    spy = spies[spyId]
    if (not spy["alive"]):
        outLines.append("ignore")
        continue

    eliminated: list[int] = []
    if dir == "N":
        eliminated = eliminateAfter(cols[spy["x"]], spy["yi"])

    elif dir == "S":
        eliminated = eliminateBefore(cols[spy["x"]], spy["yi"], "yi")

    elif dir == "E":
        eliminated = eliminateAfter(rows[spy["y"]], spy["xi"])

    elif dir == "W":
        eliminated = eliminateBefore(rows[spy["y"]], spy["xi"], "xi")

    output = str(len(eliminated)) + " " + " ".join(eliminated)
    outLines.append(output)

print("\n".join(outLines))
