# The Call for Problems for the ICPC North America Qualifier (NAQ) has finished, and a number of problems were proposed. The judges voted on the difficulty of each problem. The NAQ this year will feature some number of problems. The NAQ wants to feature problems with as many unique difficulties of possible. Compute the maximum number of unique difficulties attainable.
# # Input
# The first line of input contains two integers n and k
# NAQ will use exactly k problems out of the n proposed.
# Each of the next n lines contains a single integer k. These are the difficulties of the n problems proposed.

# Output
# Output a single integer, which is the maximum number of unique difficulties that the NAQ can feature.

# Get n/k as integers from the user
[n, k] = [int(x) for x in input().split()]

# Use an object as a map
difficulties = {}

# Loop 'n' times to get all difficulties
for i in range(n):
    difficulty = int(input())
    difficulties[difficulty] = True

# If more than 'k' unique difficulties, print k
# If less, print the number of unique difficulties found
print(min(len(difficulties), k))