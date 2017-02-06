# Uses python3
import sys

def get_fibonacci_last_digit(n):
    fiblist = []
    fiblist.insert(0,0)
    fiblist.insert(1,1)
    #modulo used to reduce memory in storage
    for i in range(2,n+1):
        fiblist.insert(i, (fiblist[i-1] + fiblist[i-2]) % 10)
    return(fiblist[n] % 10)


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
