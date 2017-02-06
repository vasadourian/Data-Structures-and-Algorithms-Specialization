def get_change(n):
    tencount = 0
    fivecount = 0
    onecount = 0
    
    while n >= 0:
        if n - 10 >= 0:
            tencount += 1
            n -= 10
        elif n - 5 >= 0:
            fivecount += 1
            n -= 5
        elif n - 1 >= 0:
            onecount +=1
            n -= 1
        else:
            break

         
    return int(tencount + fivecount + onecount)

if __name__ == '__main__':
    n = int(raw_input('Enter a number: '))
    print(get_change(n))
