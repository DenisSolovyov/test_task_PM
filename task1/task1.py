n, m = int(input()), int(input())
lst = (n - 1) * [i for i in range(1, n + 1)] + [1]
intervals = []
while lst:
    interval = lst[:m]
    intervals.append(interval)
    if interval[-1] == 1:
        break
    lst = lst[m - 1:]
result = ""
for i in intervals:
    result += str(i[0])
print(result)
