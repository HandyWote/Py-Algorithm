a = str(input())
two = 'abc'
three = 'def'
four = 'ghi'
five = 'jkl'
six = 'mno'
seven = 'pqrs'
eight = 'tuv'
nine = 'wxyz'
ans = 0
for i in a:
    if i in two:
        for j in two:
            if j != i:
                ans += 1
            else:
                ans += 1
                break
    if i in three:
        for j in three:
            if j != i:
                ans += 1
            else:
                ans += 1
                break
    if i in four:
        for j in four:
            if j != i:
                ans += 1
            else:
                ans += 1
                break
    if i in five:
        for j in five:
            if j != i:
                ans += 1
            else:
                ans += 1
                break
    if i in six:
        for j in six:
            if j != i:
                ans += 1
            else:
                ans += 1
                break
    if i in seven:
        for j in seven:
            if j != i:
                ans += 1
            else:
                ans += 1
                break
    if i in eight:
        for j in eight:
            if j != i:
                ans += 1
            else:
                ans += 1
                break
    if i in nine:
        for j in nine:
            if j != i:
                ans += 1
            else:
                ans += 1
                break
    if i == ' ':
        ans += 1
print(ans)