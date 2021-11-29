from math import ceil, floor

nums = input()

average = floor(sum(nums) / len(nums))

res = 0
for i in nums:
    res += abs(i - average)

print(res)
