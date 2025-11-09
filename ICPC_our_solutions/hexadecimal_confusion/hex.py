N = int(input())

minsum = 0
maxsum = 0

for i in range(N):
    hexstr = input()

    # Find max (0 -> D, 8 -> B)
    maxHex = hexstr.replace("0", "D").replace("8", "B")
    maxsum += int(maxHex, 16)

    # Find min (D -> 0, 8 -> B; Ignore leading 0s)
    
    # Min of 0; IGNORE!
    if (hexstr == "0" or hexstr == "D"):
        continue

    leading = hexstr[0]
    if (hexstr[0] == "0"):
        hexstr = "D" + hexstr[1:]
    
    hexstr = hexstr.replace("B", "8")
    hexstr = hexstr[0] + hexstr[1:].replace("D", "0")
    minsum += int(hexstr, 16)

print(hex(maxsum)[2:])
print(hex(minsum)[2:])