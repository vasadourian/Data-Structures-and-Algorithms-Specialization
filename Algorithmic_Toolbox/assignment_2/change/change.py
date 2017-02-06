# Uses python3
import sys

def get_change(n):
    #write your code here  
    while n > 0:
        term_count = 0
        if n - 10 > 0:
            n -= 10
            term_count += 1
            continue
        elif n - 5 > 0:
            n -= 5
            term_count += 1
            continue
        else:
            n - 1
            term_count += 1
            continue
    return term_count

if __name__ == '__main__':
    n = int(input())
    print(get_change(n))
