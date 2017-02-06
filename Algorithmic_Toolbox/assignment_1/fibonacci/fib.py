# Uses python3
def calc_fib(n):
    fiblist = []
    fiblist.insert(0,0)
    fiblist.insert(1,1)
    for i in range(2,n+1):
        fiblist.insert(i, fiblist[i-1] + fiblist[i-2])
    return fiblist[n]

n = int(input())
print(calc_fib(n))
