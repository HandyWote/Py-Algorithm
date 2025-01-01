from functools import cmp_to_key

def com(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

def lnum(numbers):
    numbers = [str(num) for num in numbers]
    numbers.sort(key=cmp_to_key(com))
    largest = ''.join(numbers)
    return largest

n = int(input())
numbers = list(map(int, input().split()))

print(lnum(numbers))