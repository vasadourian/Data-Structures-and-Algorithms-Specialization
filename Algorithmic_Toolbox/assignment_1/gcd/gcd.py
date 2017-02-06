# Uses python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    else:        
        a_prime = a % b
        a = b
        b = a_prime
        return gcd(a,b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
