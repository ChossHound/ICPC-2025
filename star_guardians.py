# https://naq25.kattis.com/contests/naq25/problems/starguardians

# !IMPORTANT
# This problem is solved via solely brute force
# This is ok as the number of star guardians is limited to 10
# No optimizations needed: This works
# Could it be more effecient? Probably.
# But we don't need to care!

# Get # of guardians
n = int(input())

# Get nummber of extra problems solved for a given team size
teamwork_sols = [int(x) for x in input().split()]

# Get the number of problems each guardian can solve alone
individual_sols = [int(x) for x in input().split()]

# member_ct: # of members to add
# members: Members in the team
# last_index: the index of the last member added
def get_max_score(member_ct: int, members: list[int], last_index = -1):
    
    # Got all team members; Compute score
    if (member_ct <= 0):
        score = teamwork_sols[len(members) - 1] # Account for teamwork
        for i in members:
            score += individual_sols[i] # Account for individual additions
        
        # Give average score contribution per member
        return score / len(members)

    max_score = 0

    # Try all team members not yet tried
    # Save maximum score attained
    for i in range(last_index + 1, n):
        
        # Create new list, and add candidate
        new_members = members.copy()
        new_members.append(i)

        max_score = max(get_max_score(member_ct - 1, new_members, i), max_score)
    
    return max_score
        
# Try all number of members
max_score = 0
for i in range(1, n + 1):
    max_score = max(get_max_score(i, []), max_score)

print(max_score)

