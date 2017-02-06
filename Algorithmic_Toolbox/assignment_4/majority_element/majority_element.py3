# Uses python3
import sys

def get_majority_element(a, left, right):
    majority_position = 0
    count = 1
    for i in range(1, right):
        
        if a[i] == a[majority_position]:
            count += 1    

        else:
            count -= 1

        if count == 0:
            majority_position = i
            count = 1

    count = 0
    for i in range(right):
        if a[i] == a[majority_position]:
            count += 1

    if count > right // 2:
        return a[majority_position]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
