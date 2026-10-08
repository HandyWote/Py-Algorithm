import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    _, q = map(int, input().split())
    a = list(map(int, input().split()))
    missions = deque()
    for _ in range(q):
        temp = list(map(int, input().split()))
        missions.append(temp)
    return a, missions

def mission1(a: list, l: int, r: int, x: int):
    l -= 1
    for i in range(l, r):
        a[i] += x


def mission2(a: list, l: int, r: int, x: int):
    l -= 1
    for i in range(l, r):
        if a[i] > x: 
            a[i] = x


def mission3(a: list, l: int, r: int):
    l -= 1
    print(sum(a[l:r]))

    
def main():
    a, missions = get_input()
    while(missions):
        i = missions.popleft()
        type, params = i[0], i[1:]
        if type == 1:
            mission1(a, *params)
        elif type == 2:
            mission2(a, *params)
        else:
            mission3(a, *params)

if __name__ == '__main__':
    main()