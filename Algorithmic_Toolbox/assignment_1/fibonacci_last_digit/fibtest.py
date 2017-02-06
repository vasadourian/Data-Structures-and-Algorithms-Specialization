# Uses python3
def get_fibonacci_last_digit(n):
    fiblist = []
    fiblist.insert(0,0)
    fiblist.insert(1,1)
    for i in range(2,n+1):
        fiblist.insert(i, fiblist[i-1] + fiblist[i-2])
    lastdigit = str(fiblist[-1])
    return(lastdigit[-1])



n = int(input())
print(get_fibonacci_last_digit(n))
