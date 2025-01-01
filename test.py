def move(s : str):
    stayy,stayx,face = 0,0,0
    for c in s:
        if c == 'F':
            if face == 0:
                stayy -= 1
            if face == 1:
                stayx += 1
            if face == 2:
                stayy += 1
            if face == 3:
                stayx -= 1
        if c == 'L':
            if face == 0:
                stayx -= 1
            if face == 1:
                stayy -= 1
            if face == 2:
                stayx += 1
            if face == 3:
                stayy -= 1
            face = (face + 4 - 1) % 4
        if c == 'R':
            if face == 0:
                stayx+= 1
            if face == 1:
                stayy += 1
            if face == 2:
                stayx -= 1
            if face == 3:
                stayy -= 1
            face = (face + 4 + 1) % 4
    return (stayy,stayx)

n = int(input())
m  = list(input())
ans = set()
t = 'LRF'
for i in range(n):
    m1 = m
    for c in t:
        m1[i] = c
        ans.add(move(str(m1)))
print(len(ans))