import sys
from math import floor

file = sys.argv[1]

nums = []

with open(file) as f:
    for line in f.readlines():
        nums.append(int(line))

average = floor(sum(nums) / len(nums))

res = 0
for i in nums:
    res += abs(i - average)

print(res)
