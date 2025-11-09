nums = [int(x) for x in input().split()]
# W, K, C
W = nums[0]
K = nums[1]
C = nums[2]


sum = 0
iter_k = K
while iter_k > 1:
    sum += iter_k-1
    iter_k -= C
sum += 1

if W < K or W > sum:
    print("no")
else:
    print("yes")

