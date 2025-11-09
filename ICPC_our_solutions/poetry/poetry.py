applicants, slots = [int(x) for x in input().split()]
import random
# Is a > b ?
def compare(a: int, b: int) -> bool:
    print(f"? {a} {b}",flush=True)
    return int(input()) == a

def tell(arr: list[int]) -> None:
    out = " ".join([str(x) for x in arr])
    print(f"! {out}", flush=True)

def qsort(people: list[int], size: int) -> list[int]:
    pivotI = 0


    if (len(people) >= 3):
        pivotI = median_of_3(people)

    pivot = people[pivotI]

    greater = []
    lesser = []

    # Get all elements > pivot
    for (i, person) in enumerate(people):
        
        # Ignore pivot
        if (i == pivotI):
            continue

        if (compare(person, pivot)):
            greater.append(person)
        else:
            lesser.append(person)
    
    if (len(greater) >= size):
        return qsort(greater, size)
    
    # Size matches exactly!
    elif (len(greater) == size):
        return greater
    
    # Include pivot
    elif (len(greater) + 1 == size):
        greater.append(pivot)
        return greater

    # Not enough people; Need to include lower-level scrubs
    else:

        # Want lesser people s.t. pros + pivot + qsort(lessers) = size
        subgreaters = qsort(lesser, size - (len(greater) + 1))
        
        return greater + [pivot] + subgreaters


def median_of_3(people: list[int])-> int:
    i = random.randint(0, len(people)-1)
    j = random.randint(0, len(people)-1)

    k = (i + j) // 2
    
    # Avoid duplicates
    if (k == min(i, j) or i == j):
        return i

    q1 = compare(people[i], people[j])
    q2 = compare(people[k], people[j])
    q3 = compare(people[i], people[k])

    if q1 == q3:
        return q2
    elif q1 == q2:
        return q3
    else:
        return q1



# People Applicants!
papplicants = []
for i in range(applicants):
    papplicants.append(i + 1)

top = qsort(papplicants, slots)

min = top[0]

# Find minimum
for (i, x) in enumerate(top):
    if (i == 0):
        continue
    
    for j in range(i + 1, len(top)):
        if (compare(x, top[j])):
            break
    else:
        if not (compare(x, min)):
            min = x

for i in papplicants:
    if (i == min):
        continue

    compare(i, min)

tell(top)
