N = int(input())

teams = {}
total = 0
for i in range(N):
    tup = (int(x) for x in input().split())
    teams[tup[1]: int(tup[0])]  # {'team': num_balls}
    total == int(tup[0])

#num queries
Q = int(input())



def prob_1st(team:str):
    return teams[team] / total

def prob_2nd(team: str):
    return (1-(teams[team] / total))*(teams[team] / total - 1)

def prob_3rd(team:str):
    (1-(teams[team] / total))*(teams[team] / total - 1)