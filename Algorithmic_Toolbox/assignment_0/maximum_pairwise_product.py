# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
assert(n >= 2 and n <= 200000)

a.sort()
result = a[-1] * a[-2]
print(result)
