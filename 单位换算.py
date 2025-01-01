def is_n(s):
    for i, char in enumerate(s):
        try:
            int(char)
        except ValueError:
            return int(s[:i]), s[i:]
d = {
    'GB' : 2**30,
    'MB' : 2**20,
    'KB' : 2**10,
    'B' : 1
}

a = input().split("=?")
numnow,goal = a[0],a[1]
num,now = is_n(numnow)

ans = float(num * (d[now]/d[goal]))

print("%.6f" % ans)