from collections import deque

def main():
    s = input()
    s = function(s)
    if s: print(s)
    else: print('!!!!')

def function(s):
    que = deque()
    for i in s:
        if i == 'D':
            if que:
                que.pop()
        else:
            que.append(i)
    return ''.join(que)

if __name__ == '__main__':
    main()