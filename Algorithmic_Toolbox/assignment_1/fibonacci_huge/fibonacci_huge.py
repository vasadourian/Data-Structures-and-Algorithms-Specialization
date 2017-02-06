# Uses python3
import sys
def calc_fib(n):
    fiblist = []
    fiblist.insert(0,0)
    fiblist.insert(1,1)
    for i in range(2,n+1):
        fiblist.insert(i, fiblist[i-1] + fiblist[i-2])
    return fiblist[n]

def get_fibonaccihuge(n, m):
    return calc_fib(n) % m
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonaccihuge(n, m))
