import math
from functools import reduce

N = int(input())

def gcd_list(nums):
    return reduce(math.gcd, nums)

total = 0

for a in range(N):
    for b in range(N):
        for c in range(N):
            total += gcd_list([a+1, b+1, c+1])

print(total)
