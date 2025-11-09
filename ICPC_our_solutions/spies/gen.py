spies = 0

teams = 300000

lines: list[str] = []

lines.append(f"{teams} {teams}")

# Team def
for i in range(teams):
    lines.append(f"{i} 1")

# Turn def
# for i in range(teams - 1, -1, -1):
#     lines.append(f"{i + 1} E")

# First should kill EVERYONE!
for i in range(teams):
    lines.append(f"{i + 1} W")

file = open("./gened.txt", "w+")
file.write("\n".join(lines))
file.close()
