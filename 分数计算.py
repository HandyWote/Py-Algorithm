a,b,c,d,e,f = map(int,input().split())
ans = 0
for x in [a, b, c]:
    if x< 60:
        ans += 1
if ans<= 1:
    print('PASS')
else:
    print ("FAIL")
ans=(a*d+b*e+c*f)/(d+e+f)
if ans< 60:
    print ("FAIL")
else:
    print ("PASS")